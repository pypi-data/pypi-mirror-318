from typing import Any, Optional


class BaseCall:
    # BUILD
    def set_stdin(self, value):
        """Set the stdin for the call."""
        raise NotImplementedError

    def __or__(self, other: "BaseCall") -> "BaseCall":
        from .pipe import Pipe

        calls = []
        if isinstance(self, Pipe):
            calls.extend(self.calls)
        else:
            calls.append(self)
        if isinstance(other, Pipe):
            calls.extend(other.calls)
        else:
            calls.append(other)

        return Pipe(calls=calls)

    def clone(self) -> "BaseCall":
        raise NotImplementedError

    # EXECUTION
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        # should be called last
        # once this is called, no mutation should be allowed
        raise NotImplementedError

    # WAIT FOR COMPLETION
    def wait(self, timeout: float = None):
        raise NotImplementedError

    # corresponding IO file objects, only available after __call__
    @property
    def stdout(self):  # should always be PIPE
        raise NotImplementedError

    @property
    def stderr(self):  # should always be PIPE
        raise NotImplementedError

    @property
    def stdin(self):
        raise NotImplementedError

    # RESULT
    @property
    def out(self) -> Optional[bytes]:
        raise NotImplementedError

    @property
    def err(self) -> Optional[bytes]:
        raise NotImplementedError

    @property
    def returncode(self) -> Optional[int]:
        raise NotImplementedError

    def ok(self, timeout: float = None):
        """Invoke the command and wait for successful completion.
        Returns the stdout as bytes.
        """
        self.__call__()
        self.out  # noqa
        self.wait(timeout=timeout)
        if self.returncode != 0:
            raise RuntimeError(f"return code: {self.returncode}")

        if not self.stdout:
            return None
        return self.out
