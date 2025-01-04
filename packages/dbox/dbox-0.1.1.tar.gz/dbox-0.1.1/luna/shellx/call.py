import io
import logging
import subprocess
from functools import cached_property
from typing import IO, Any, List, Optional, Union

from .base import BaseCall
from .ctx import current_shell_context

log = logging.getLogger(__name__)


class Call(BaseCall):
    def __init__(
        self, cmds: List[str], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **popen_kwargs
    ):
        self.cmds: List[str] = cmds
        self._popen_kwargs = popen_kwargs

        self.process: subprocess.Popen = None
        self._stdin = stdin
        self._stdout = stdout
        self._stderr = stderr
        # is this really faster

    def __repr__(self):
        return f"Call({', '.join(self.cmds)})"

    def set_stdin(self, value):
        assert self.process is None, "Should only be called once before __call__"
        self._stdin = value

    def no_stderr(self):
        # assert self._stderr is None
        self._stderr = subprocess.STDOUT
        return self

    def clone(self) -> BaseCall:
        return Call(self.cmds)

    def __call__(self, stdin: Optional[Union[bytes, str, IO]] = None) -> Any:
        if self.process is not None:
            raise ValueError("Cannot call a process twice")
        # if stdin is not None:
        if isinstance(stdin, io.BufferedReader):
            self._stdin = stdin
        self.process = subprocess.Popen(
            self.cmds,
            stdin=self._stdin,
            stdout=self._stdout,
            stderr=self._stderr,
            # bufsize=819200,
            **self._popen_kwargs,
        )
        log.debug("Started process %s", self)
        self.shell_context = current_shell_context()
        self.shell_context.add_pid(self.process.pid)
        self._stdout = self.process.stdout
        self._stderr = self.process.stderr
        if isinstance(stdin, (str, bytes)):
            # might block
            stdin = stdin.encode("utf-8") if isinstance(stdin, str) else stdin
            self.process.stdin.write(stdin)
            self.process.stdin.close()

    def wait(self, timeout: float = None):
        # if we do not read from stdout then this will block
        if self.process.returncode is not None:
            return
        self.process.wait(timeout=timeout)
        log.debug("Process %s finished", self)
        self.shell_context.mark_completed(self.process.pid)
        del self.shell_context

    @cached_property
    def out(self) -> Optional[bytes]:
        if self.process.stdout is None:
            return None  # no stdout
        return self.process.stdout.read()

    @cached_property
    def err(self) -> Optional[bytes]:
        if self.process.stderr is None:
            return None  # no stderr
        return self.process.stderr.read()

    @property
    def returncode(self) -> Optional[int]:
        return self.process.poll()

    @property
    def stdout(self):
        return self.process.stdout

    @property
    def stderr(self):
        return self.process.stderr

    @property
    def stdin(self):
        return self.process.stdin
