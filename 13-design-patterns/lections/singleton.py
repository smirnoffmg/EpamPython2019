class Singleton:
    __instance = None

    def __init__(self):
        if Singleton.__instance is None:
            Singleton.__instance = self
        else:
            raise Exception('The class is a singleton')

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            return Singleton()
        return Singleton.__instance

    @staticmethod
    def useful_function():
        return 42


if __name__ == '__main__':
    print(Singleton())
    # print(Singleton())  # Второй вызов констуктора выдаст ошибку
    print(Singleton.get_instance())
    print(Singleton.get_instance())
    print(Singleton.get_instance().useful_function())
