from contextlib import contextmanager
from contextvars import ContextVar
from typing import Any, Dict, TypeVar

_CTX: ContextVar[Dict[str, Any]] = ContextVar("ctx", default=None)


@contextmanager
def set_context(**kwargs):
    try:
        ctx = _CTX.get() or {}
        new_ctx = {**ctx, **kwargs}
        token = _CTX.set(new_ctx)
        yield
    finally:
        _CTX.reset(token)


_MISSING = object()


def use(key: str, default=_MISSING) -> Any:
    curr = _CTX.get()
    if key not in curr and default is _MISSING:
        raise RuntimeError("no such context key %s provided" % key)
    return curr.get(key, default)


T = TypeVar("T")


def use_factory(tpe: type[T], key: str):
    def use_context(default=_MISSING) -> T:
        ctx = _CTX.get()
        if key not in ctx and default is _MISSING:
            raise RuntimeError("no such context key %s provided" % key)
        curr = ctx.get(key, default)
        # assert isinstance(curr, tpe)
        return curr

    return use_context
