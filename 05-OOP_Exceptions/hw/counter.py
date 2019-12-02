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
    setattr(cls, 'count_obj', 0)
    origin_init = cls.__init__

    def increment_count_obj(*args, **kwargs):
        cls.count_obj += 1
        origin_init(*args, **kwargs)

    def get_created_instances(*args, **kwargs):
        return cls.count_obj

    def reset_instances_counter(*args, **kwargs):
        result, cls.count_obj = cls.count_obj, 0
        return result

    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter
    cls.__init__ = increment_count_obj

    return cls

@instances_counter
class User:
    pass


if __name__ == '__main__':

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
