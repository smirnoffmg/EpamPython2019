"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    cls.counter = 0

    def __init__(self, *args, **kwargs):
        cls.counter += 1

    def get_created_instances(*args, **kwargs):
        return cls.counter

    def reset_instances_counter(*args, **kwargs):
        old_value = cls.counter
        cls.counter = 0
        return old_value

    cls.__init__ = __init__
    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter

    return cls


@instances_counter
class User:
    pass


if __name__ == '__main__':

    User.get_created_instances()  # 0
    print(User.get_created_instances())
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3