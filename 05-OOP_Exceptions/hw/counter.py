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
    setattr(cls, "counter", 0)

    def __init__(self):
        cls.counter += 1

    def get_created_instances(self=None):
        return cls.counter

    def reset_instances_counter(self=None):
        cls.counter -= 1

    setattr(cls, "__init__", __init__)
    setattr(cls, "get_created_instances", get_created_instances)
    setattr(cls, "reset_instances_counter", reset_instances_counter)

    return cls


@instances_counter
class User:
    pass


if __name__ == '__main__':
    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
