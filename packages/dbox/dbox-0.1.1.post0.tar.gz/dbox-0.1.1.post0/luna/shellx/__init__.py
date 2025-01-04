# ruff: noqa: F401
from .base import BaseCall
from .call import Call
from .ctx import shell_context
from .pipe import Pipe


def cmd(*cmds, **kwargs):
    """Create a command object. For advanced usage, such as allow running in backgroud, pipe, etc."""
    cl = Call(cmds, stderr=None, **kwargs)
    return cl


def fire(*cmds, **kwargs) -> None:
    """Create a command object, execute it, ensure it completed successfully.
    No PIPE will be created.
    """
    cl = Call(cmds, stdin=None, stdout=None, stderr=None, **kwargs)
    cl.ok()


def invoke(*cmds, **kwargs) -> bytes:
    """Create a command object, execute it, ensure it completed successfully.
    The stdout will be captured and returned as bytes. No other PIPE will be created."""
    cl = Call(cmds, stdin=None, stderr=None, **kwargs)
    return cl.ok()
