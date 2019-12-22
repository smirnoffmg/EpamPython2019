def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_instance


@singleton
class UsefulClass:
    pass


instance_1 = UsefulClass()
instance_2 = UsefulClass()
instance_3 = UsefulClass()

print(instance_1 is instance_2 is instance_3)  # True
