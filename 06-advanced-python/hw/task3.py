"""
Реализовать дескриптор, кодирующий слова с помощью шифра Цезаря

"""


class ShiftDescriptor:

    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass


class CeasarSipher:

    message = ShiftDescriptor(4)
    another_message = ShiftDescriptor(7)


a = CeasarSipher()
a.message = 'abc'
a.another_message = 'hello'

assert a.message == 'efg'
assert a.another_message == 'olssv'