""""
Реализовать контекстный менеджер, который подавляет переданные исключения
with Suppressor(ZeroDivisionError):
    1/0
print("It's fine")
"""


class Suppressor:
    """Suppressor context manager locally
    suppresses exceptions of specified types"""

    def __init__(self, *press_some_exception):
        self.press_exception = press_some_exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return (exc_type is not None and
                issubclass(exc_type, self.press_exception))


with Suppressor(ZeroDivisionError):
    a = 1/0
print("It is fine")


