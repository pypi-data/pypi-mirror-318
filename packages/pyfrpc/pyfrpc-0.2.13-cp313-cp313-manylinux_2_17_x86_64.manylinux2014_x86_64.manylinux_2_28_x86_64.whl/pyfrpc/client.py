# -*- coding: utf-8 -*-

import xmlrpc.client
from functools import wraps
from http.cookiejar import CookiePolicy
from typing import Any, Dict, Optional, Tuple

import requests
from requests import Session

from .coding import decode, encode
from .models import FrpcCall, FrpcFault, FrpcResponse

APPLICATION_FRPC = "application/x-frpc"


def cached_getter(func):
    key = "__cache_{:x}".format(id(func))

    @wraps(func)
    def new_func(self):
        if not hasattr(self, key):
            setattr(self, key, func(self))

        return getattr(self, key)

    return new_func


class BlockAllCookiePolicy(CookiePolicy):
    set_ok = return_ok = domain_return_ok =  path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = False
    hide_cookie2 = False


class FrpcClient(object):
    def __init__(
        self,
        url: str,
        *,
        cert: Optional[Tuple[str,str]] = None,
        verify: bool = True,
        timeout: float = 60.0,
        session: Optional[Session] = None,
        version: int = 0x0201,
        req_opts: Optional[Dict[str, Any]] = None
    ) -> None:
        self._url = url
        self._version = version

        if session:
            self.session = session
        else:
            self.session = requests.session()
            self.session.cookies.set_policy(BlockAllCookiePolicy())
            self.session.verify = verify

            if cert:
                if cert[1]:
                    self.session.cert = cert
                else:
                    self.session.cert = cert[0]

        self._opts = req_opts or {}
        self._opts.setdefault("timeout", timeout)

    def call(self, method, args=(), **kwargs):
        payload = encode(FrpcCall(name=method, args=args), self._version)

        headers = kwargs.pop('headers', {})
        headers.update({
            "Content-Type" : APPLICATION_FRPC,
            "Accept" : APPLICATION_FRPC,
        })

        for k,v in self._opts.items():
            kwargs.setdefault(k, v)

        res = self.session.request("POST", self._url, data=payload, headers=headers, **kwargs)

        if res.status_code != 200:
            raise RuntimeError("bad status code, expected 200, got {:d}".format(res.status_code))

        content_type = res.headers.get("Content-Type", None)

        # FRPC decoding
        if content_type == APPLICATION_FRPC:
            payload = decode(res.content)

            if isinstance(payload, FrpcFault):
                raise payload

            return payload.data

        # XML-RPC decoding
        if content_type == "text/xml":
            try:
                payload, _ = xmlrpc.client.loads(
                    res.content, use_datetime=True, use_builtin_types=True)
                return payload[0]
            except xmlrpc.client.Fault as e:
                raise FrpcFault(e.faultCode, e.faultString)

        raise RuntimeError("bad content type: " + content_type)

    @cached_getter
    def methods(self):
        try:
            return self.call("system.listMethods")
        except:
            return []

    def help(self, method):
        return self.call("system.methodHelp", (method,))

    @property
    def rpc(self):
        return _FrpcClientAttr(self, "")

    @property
    def url(self):
        return self._url


class _FrpcClientAttr(object):
    def __init__(self, client, method):
        self._client = client
        self._method = method

        self._prefix = self._method + ("." if self._method else "")

    def __getattr__(self, name):
        if name.startswith("__"):
            return super().__getattr__(name)

        method = self._prefix + name
        return _FrpcClientAttr(self._client, method)

    def __call__(self, *args, **kwargs):
        return self._client.call(self._method, args, **kwargs)

    @property
    @cached_getter
    def __doc__(self):
        try:
            return self._client.help(self._method)
        except Exception as e:
            return "Failed to get method documentation.\n\n{}".format(e)
        except:
            return "Failed to get method documentation."

    @cached_getter
    def __dir__(self):
        methods = self._client.methods()

        methods = [m for m in methods if m.startswith(self._prefix)]
        methods = [m[len(self._prefix):] for m in methods]
        methods = [m.split(".", 1)[0] for m in methods]
        methods = list(set(methods))

        return methods
