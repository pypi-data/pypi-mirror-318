import logging
from typing import Any, List, Optional

from .base import BaseCall

log = logging.getLogger(__name__)


class Pipe(BaseCall):
    def __init__(self, calls: List[BaseCall]):
        assert calls
        self.calls = calls

    def set_stdin(self, value):
        self.calls[0].stdin = value

    def clone(self) -> BaseCall:
        return Pipe([call.clone() for call in self.calls])

    def __repr__(self):
        return "Pipe{}".format(self.calls)

    def __call__(self, stdin: Optional[bytes] = None) -> Any:
        prev_stdout = None
        for i, call in enumerate(self.calls):
            # call.stdout = subprocess.PIPE
            if i > 0:
                call.set_stdin(prev_stdout)
                call()
            else:
                call(stdin=stdin)
            prev_stdout = call.stdout
        for call in self.calls[:-1]:
            call.stdout.close()

    def wait(self, timeout: float = None, capture_stdout: bool = True):
        for call in self.calls:
            call.wait(timeout=timeout)

    @property
    def out(self):
        self.wait()
        # note that in pipe, we can only get the last call's output
        return self.calls[-1].out

    @property
    def err(self):
        self.wait()
        return self.calls[-1].err

    @property
    def returncode(self):
        # until all calls are done
        for call in self.calls:
            if call.returncode is None:
                return None
        # the first non-zero return code
        for call in self.calls:
            if call.returncode != 0:
                log.debug("Pipe return code: %s from %s", call.returncode, call)
                return call.returncode
        return 0

    @property
    def stdin(self):
        return self.calls[0].stdin

    @property
    def stdout(self):
        return self.calls[-1].stdout

    @property
    def stderr(self):
        return self.calls[-1].stderr

    def __getitem__(self, index):
        return self.calls[index]

    def __iter__(self):
        return iter(self.calls)
