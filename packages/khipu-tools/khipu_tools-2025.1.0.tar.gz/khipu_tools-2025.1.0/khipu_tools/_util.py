import functools
import hmac
import logging
import os
import re
import sys
from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Optional,
    TypeVar,
    Union,
    cast,
    overload,
)
from urllib.parse import parse_qsl, quote_plus

import typing_extensions

# Used for global variables
import khipu_tools
from khipu_tools._api_mode import ApiMode

if TYPE_CHECKING:
    from khipu_tools._api_requestor import _APIRequestor
    from khipu_tools._khipu_object import KhipuObject
    from khipu_tools._khipu_response import KhipuResponse

KHIPU_LOG = os.environ.get("KHIPU_LOG")

logger: logging.Logger = logging.getLogger("khipu")


deprecated = typing_extensions.deprecated


def _console_log_level():
    if khipu_tools.log in ["debug", "info"]:
        return khipu_tools.log
    elif KHIPU_LOG in ["debug", "info"]:
        return KHIPU_LOG
    else:
        return None


def log_debug(message, **params):
    msg = logfmt(dict(message=message, **params))
    if _console_log_level() == "debug":
        print(msg, file=sys.stderr)
    logger.debug(msg)


def log_info(message, **params):
    msg = logfmt(dict(message=message, **params))
    if _console_log_level() in ["debug", "info"]:
        print(msg, file=sys.stderr)
    logger.info(msg)


def logfmt(props):
    def fmt(key, val):
        # Handle case where val is a bytes or bytesarray
        if hasattr(val, "decode"):
            val = val.decode("utf-8")
        # Check if val is already a string to avoid re-encoding into
        # ascii. Since the code is sent through 2to3, we can't just
        # use unicode(val, encoding='utf8') since it will be
        # translated incorrectly.
        if not isinstance(val, str):
            val = str(val)
        if re.search(r"\s", val):
            val = repr(val)
        # key should already be a string
        if re.search(r"\s", key):
            key = repr(key)
        return f"{key}={val}"

    return " ".join([fmt(key, val) for key, val in sorted(props.items())])


# Borrowed from Django's source code
if hasattr(hmac, "compare_digest"):
    # Prefer the stdlib implementation, when available.
    def secure_compare(val1, val2):
        return hmac.compare_digest(val1, val2)

else:

    def secure_compare(val1, val2):
        """
        Returns True if the two strings are equal, False otherwise.
        The time taken is independent of the number of characters that match.
        For the sake of simplicity, this function executes in constant time
        only when the two strings have the same length. It short-circuits when
        they have different lengths.
        """
        if len(val1) != len(val2):
            return False
        result = 0
        if isinstance(val1, bytes) and isinstance(val2, bytes):
            for x, y in zip(val1, val2):
                result |= x ^ y
        else:
            for x, y in zip(val1, val2):
                result |= ord(cast(str, x)) ^ ord(cast(str, y))
        return result == 0


Resp = Union["KhipuResponse", dict[str, Any], list["Resp"]]


@overload
def convert_to_khipu_object(
    resp: Union["KhipuResponse", dict[str, Any]],
    api_key: Optional[str] = None,
    params: Optional[Mapping[str, Any]] = None,
    klass_: Optional[type["KhipuObject"]] = None,
    *,
    api_mode: ApiMode = "V3",
) -> "KhipuObject": ...


@overload
def convert_to_khipu_object(
    resp: list[Resp],
    api_key: Optional[str] = None,
    params: Optional[Mapping[str, Any]] = None,
    klass_: Optional[type["KhipuObject"]] = None,
    *,
    api_mode: ApiMode = "V3",
) -> list["KhipuObject"]: ...


def convert_to_khipu_object(
    resp: Resp,
    api_key: Optional[str] = None,
    params: Optional[Mapping[str, Any]] = None,
    klass_: Optional[type["KhipuObject"]] = None,
    *,
    api_mode: ApiMode = "V3",
) -> Union["KhipuObject", list["KhipuObject"]]:
    from khipu_tools._api_requestor import _APIRequestor

    return _convert_to_khipu_object(
        resp=resp,
        params=params,
        klass_=klass_,
        requestor=_APIRequestor._global_with_options(
            api_key=api_key,
        ),
        api_mode=api_mode,
    )


@overload
def _convert_to_khipu_object(
    *,
    resp: Union["KhipuResponse", dict[str, Any]],
    params: Optional[Mapping[str, Any]] = None,
    klass_: Optional[type["KhipuObject"]] = None,
    requestor: "_APIRequestor",
    api_mode: ApiMode,
) -> "KhipuObject": ...


@overload
def _convert_to_khipu_object(
    *,
    resp: list[Resp],
    params: Optional[Mapping[str, Any]] = None,
    klass_: Optional[type["KhipuObject"]] = None,
    requestor: "_APIRequestor",
    api_mode: ApiMode,
) -> list["KhipuObject"]: ...


def _convert_to_khipu_object(
    *,
    resp: Resp,
    params: Optional[Mapping[str, Any]] = None,
    klass_: Optional[type["KhipuObject"]] = None,
    requestor: "_APIRequestor",
    api_mode: ApiMode,
) -> Union["KhipuObject", list["KhipuObject"]]:
    # If we get a KhipuResponse, we'll want to return a
    # KhipuObject with the last_response field filled out with
    # the raw API response information
    khipu_response = None

    # Imports here at runtime to avoid circular dependencies
    from khipu_tools._khipu_object import KhipuObject
    from khipu_tools._khipu_response import KhipuResponse

    if isinstance(resp, KhipuResponse):
        khipu_response = resp
        resp = cast(Resp, khipu_response.data)

    if isinstance(resp, list):
        return [
            _convert_to_khipu_object(
                resp=cast("Union[KhipuResponse, Dict[str, Any]]", i),
                requestor=requestor,
                api_mode=api_mode,
                klass_=klass_,
            )
            for i in resp
        ]
    elif isinstance(resp, dict) and not isinstance(resp, KhipuObject):
        resp = resp.copy()

        klass = KhipuObject

        obj = klass._construct_from(
            values=resp,
            last_response=khipu_response,
            requestor=requestor,
            api_mode=api_mode,
        )

        # We only need to update _retrieve_params when special params were
        # actually passed. Otherwise, leave it as is as the list / search result
        # constructors will instantiate their own params.
        if (
            params is not None
            and hasattr(obj, "object")
            and ((getattr(obj, "object") == "list") or (getattr(obj, "object") == "search_result"))
        ):
            obj._retrieve_params = params

        return obj
    else:
        return cast("KhipuObject", resp)


def convert_to_dict(obj):
    """Converts a KhipuObject back to a regular dict.

    Nested KhipuObjects are also converted back to regular dicts.

    :param obj: The KhipuObject to convert.

    :returns: The KhipuObject as a dict.
    """
    if isinstance(obj, list):
        return [convert_to_dict(i) for i in obj]
    # This works by virtue of the fact that KhipuObjects _are_ dicts. The dict
    # comprehension returns a regular dict and recursively applies the
    # conversion to each value.
    elif isinstance(obj, dict):
        return {k: convert_to_dict(v) for k, v in obj.items()}
    else:
        return obj


@overload
def populate_headers(
    idempotency_key: str,
) -> dict[str, str]: ...


@overload
def populate_headers(idempotency_key: None) -> None: ...


def populate_headers(
    idempotency_key: Union[str, None],
) -> Union[dict[str, str], None]:
    return None


T = TypeVar("T")


def merge_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z


def sanitize_id(id):
    quotedId = quote_plus(id)
    return quotedId


def get_api_mode(url):
    return "V3"


class class_method_variant:
    def __init__(self, class_method_name):
        self.class_method_name = class_method_name

    T = TypeVar("T")

    method: Any

    def __call__(self, method: T) -> T:
        self.method = method
        return cast(T, self)

    def __get__(self, obj, objtype: Optional[type[Any]] = None):
        @functools.wraps(self.method)
        def _wrapper(*args, **kwargs):
            if obj is not None:
                # Method was called as an instance method, e.g.
                # instance.method(...)
                return self.method(obj, *args, **kwargs)
            elif len(args) > 0 and objtype is not None and isinstance(args[0], objtype):
                # Method was called as a class method with the instance as the
                # first argument, e.g. Class.method(instance, ...) which in
                # Python is the same thing as calling an instance method
                return self.method(args[0], *args[1:], **kwargs)
            else:
                # Method was called as a class method, e.g. Class.method(...)
                class_method = getattr(objtype, self.class_method_name)
                return class_method(*args, **kwargs)

        return _wrapper
