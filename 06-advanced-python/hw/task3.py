""""
Реализовать контекстный менеджер, который подавляет переданные исключения
with Suppressor(ZeroDivisionError):
    1/0
print("It's fine")
"""


class Suppressor:
    def __init__(self, *exceptions):
        self._exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exception_type, exception_value, traceback):
        return issubclass(exception_type, self._exceptions)


with Suppressor(ZeroDivisionError):
    1/0
print("It's fine")