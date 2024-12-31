from IPython.core.interactiveshell import InteractiveShell

from .display_hook import DisplayHook


FILENAME = "script.py"


def exception_raiser(_self: InteractiveShell, _exception_type, exception, _traceback):
    if issubclass(_exception_type, SyntaxError):
        exception.filename = f"<{FILENAME}>"
    raise exception


class WasmProcess:
    def __init__(self):
        InteractiveShell.displayhook_class = DisplayHook
        InteractiveShell._showtraceback = exception_raiser
        self.shell = InteractiveShell(user_ns={}, colors="NoColor")

    def run(self):
        pass

    def executeTask(self, task):
        return task(self.shell)

    def kill(self):
        self.reset()

    def reset(self):
        self.shell.reset()
