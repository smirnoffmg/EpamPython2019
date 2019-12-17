"""

Реализовать такой метакласс, что экземпляры класса созданного с помощью него
будут удовлетворять следующим требованиям:

* объекты созданные с одинаковыми аттрибутами будут одним и тем же объектом
* объекты созданные с разными аттрибутами будут разными объектами
* у любого объекта есть мозможность получить доступ к другим объектам
    того же класса


>>> unit1 = SiamObj('1', '2', a=1)
>>> unit2 = SiamObj('1', '2', a=1)
>>> unit1 is unit2
True
>>> unit3 = SiamObj('2', '2', a=1)
>>> unit3.connect('1', '2', 1).a = 2
>>> unit2.a == 2
True
>>> pool = unit3.pool
>>> print(len(b))
2
>>> del unit3
>>> print(len(pool))
1

"""
import weakref


class Meta(type):
    _inst = weakref.WeakSet()

    def connect(cls, *args, **kwargs):
        _args = {}
        if len(args) > 2:
            _args.update({'a': args[-1]})
            _args.update({'args': args[:-1]})
        else:
            _args.update({'args': args})
            _args.update(kwargs)
        if cls == SiamObj:
            for i in cls._inst:
                if i.__dict__ == _args:
                    return i

    def __call__(cls, *args, **kwargs):
        setattr(cls, 'connect', cls.connect)
        setattr(cls, 'pool', cls._inst)
        _cls = super().__call__(*args, **kwargs)
        for item in cls._inst:
            if type(item) != type(_cls):
                cls._inst.add(_cls)
        if isinstance(_cls, SiamObj):
            for i in cls._inst:
                if i.__dict__ == _cls.__dict__:
                    return i
            cls._inst.add(_cls)
        for i, item in enumerate(cls._inst):
            if i == len(cls._inst)-1:
                return item


class SiamObj(metaclass=Meta):
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            self.__dict__[key] = value
        if len(args) > 2:
            self.__dict__.update({'a': args[-1]})
            self.__dict__.update({'args': args[:-1]})
        else:
            self.__dict__.update({'args': args})


if __name__ == '__main__':
    test1 = SiamObj('1', '2', 1)
    test2 = SiamObj('1', '2', a=1)
    test3 = SiamObj('1', '2', a=2)
    test3.connect('1', '2', 1).a = 2
    print(test2 is test1)
    pool = test3.pool
    print(len(pool))
    del test3
    print(len(pool))




