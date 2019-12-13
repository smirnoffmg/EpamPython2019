"""
Написать свое property c кэшем и таймаутом
полностью повторяет поведение стандартной property за исключением:
    * хранит результат работы метода некоторое время, которое передается
      параметром в инициализацию проперти
    * пересчитывает значение, если таймер истек
"""

import time
import uuid


def timer_property(t=None):
    cache = []
    time_limit = time.time()
    class Property:

        def __init__(self, fget=None, fset=None, fdel=None):
            self.fget = fget
            self.fset = fset
            self.fdel = fdel

        def __get__(self, instance, owner):
            if instance is None:
                return self

            if self.fget is None:
                raise AttributeError('unreadable attribute')
            nonlocal cache
            if not cache:
                cache = self.fget(instance)
            elif (time.time() - time_limit) > 10:
                cache = self.fget(instance)
            return cache

        def __set__(self, instance, value):
            if instance is None:
                return self

            if self.fget is None:
                raise AttributeError("can't set attribute")

            nonlocal cache, time_limit
            cache = value
            time_limit = time.time()
            return self.fset(instance, value)

        def __delete__(self, instance):
            if self.fget is None:
                raise AttributeError("can't delete attribute")

            return self.fdel(instance)

        def getter(self, fget):
            return type(self)(fget, self.fset, self.fdel)

        def setter(self, fset):
            return type(self)(self.fget, fset, self.fdel)

        def deleter(self, fdel):
            return type(self)(self.fget, self.fset, fdel)

    return Property


class Message:

    @timer_property(t=10)
    def msg(self):
        self._msg = self.get_message()
        return self._msg

    @msg.setter # reset timer also
    def msg(self, param):
        self._msg = param

    def get_message(self):
        """
        Return random string
        """
        return uuid.uuid4().hex


if __name__ == '__main__':
    m = Message()
    message = m.msg
    print(m.msg == message)
    time.sleep(1)
    print(m.msg == message)
    m.msg = 'test_message'
    print(m.msg != message)
    message = m.msg
    time.sleep(1)
    print(m.msg == message)
    # m.msg = 'test_message'
    # initial = m.msg
    # assert initial is m.msg
    # time.sleep(10)
    # assert initial is not m.msg
