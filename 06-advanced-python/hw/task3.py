""""
Реализовать контекстный менеджер, который подавляет переданные исключения
with Suppressor(ZeroDivisionError):
    1/0
print("It's fine")
"""

import sys
from contextlib import suppress


class Suppressor:
    """Suppressor context manager locally
    suppresses exceptions of specified types"""

    def __init__(self, *press_some_exception):
        self.press_exception = press_some_exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        # we want to check only when an exception occurred,
        # therefore an additional condition exc_type is not None
        return exc_type is not None and issubclass(exc_type, self.press_exception)


with Suppressor(ZeroDivisionError):
    a = 1/0
print("It is fine")


class Withoutsuppress:
    """Example class used to demonstrate contextlib.suppress work"""

    def __enter__(self):
        print("Enter to context")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(sys.exc_info())
        print("Exit context")


with suppress(ZeroDivisionError):  # that construction also suppresses any of the specified exceptions
    with Withoutsuppress():
        raise ZeroDivisionError


class Suppressor:
    pass

