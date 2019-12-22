from abc import ABC, abstractmethod


class AbstractProductA(ABC):  # колесо
    """
    Каждый отдельный продукт семейства продуктов должен иметь базовый интерфейс.
    Все вариации продукта должны реализовывать этот интерфейс.
    """

    @abstractmethod
    def useful_function_a(self) -> str:  # надуть колесо
        pass


"""
Конкретные продукты создаются соответствующими Конкретными Фабриками.
"""


class ConcreteProductA1(AbstractProductA):  # колесо автомобиля
    def useful_function_a(self) -> str:  # надуть колесо
        return "The result of the product A1."


class ConcreteProductA2(AbstractProductA):  # колесо велосипеда
    def useful_function_a(self) -> str:  # надуть колесо
        return "The result of the product A2."


class AbstractProductB(ABC):  # средство передвижения
    """
    Базовый интерфейс другого продукта. Все продукты могут взаимодействовать
    друг с другом, но правильное взаимодействие возможно только между продуктами
    одной и той же конкретной вариации.
    """
    @abstractmethod
    def useful_function_b(self) -> None:  # ехать
        """
        Продукт Б способен работать самостоятельно...
        """
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:  # установить колесо
        """
        ...а также взаимодействовать с Продуктами А той же вариации.

        Абстрактная Фабрика гарантирует, что все продукты, которые она создает,
        имеют одинаковую вариацию и, следовательно, совместимы.
        """
        pass


"""
Конкретные Продукты создаются соответствующими Конкретными Фабриками.
"""


class ConcreteProductB1(AbstractProductB):  # конкретное средство передвижения: автомобиль
    def useful_function_b(self) -> str:  # ехать
        # проверить колеса: если надо, установить и надуть колеса
        # завести двигатель
        # нажать на педаль газа
        return "The result of the product B1."

    """
    Продукт Б1 может корректно работать только с Продуктом A1. Тем не менее, он
    принимает любой экземпляр Абстрактного Продукта А в качестве аргумента.
    """

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:  # установить колесо(абстрактное колесо)
        result = collaborator.useful_function_a()  # надули колесо
        return f"The result of the B1 collaborating with the ({result})"


class ConcreteProductB2(AbstractProductB):  # конкретное средство передвижения: велосипед
    def useful_function_b(self) -> str:  # ехать
        # проверить колеса: если надо, установить и надуть колеса
        # снять замок
        # крутить педали
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductA):  # установить колесо(абстрактное колесо)
        """
        Продукт Б2 может корректно работать только с Продуктом A2. Тем не менее,
        он принимает любой экземпляр Абстрактного Продукта А в качестве
        аргумента.
        """
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"


class AbstractFactory(ABC):
    """
    Интерфейс Абстрактной Фабрики объявляет набор методов, которые возвращают
    различные абстрактные продукты. Эти продукты называются семейством и связаны
    темой или концепцией высокого уровня. Продукты одного семейства обычно могут
    взаимодействовать между собой. Семейство продуктов может иметь несколько
    вариаций, но продукты одной вариации несовместимы с продуктами другой.
    """
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:  # создать колесо
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:  # создать средство передвижения
        pass


class ConcreteFactory1(AbstractFactory):  # будем работать с автомобилем
    """
    Конкретная Фабрика производит семейство продуктов одной вариации. Фабрика
    гарантирует совместимость полученных продуктов. Обратите внимание, что
    сигнатуры методов Конкретной Фабрики возвращают абстрактный продукт, в то
    время как внутри метода создается экземпляр конкретного продукта.
    """

    def create_product_a(self) -> ConcreteProductA1:  # создать колесо автомобиля
        return ConcreteProductA1()

    def create_product_b(self) -> ConcreteProductB1:  # создать автомобиль
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):  # будем работать с велосипедом
    """
    Каждая Конкретная Фабрика имеет соответствующую вариацию продукта.
    """

    def create_product_a(self) -> ConcreteProductA2:  # создать колесо велосипеда
        return ConcreteProductA2()

    def create_product_b(self) -> ConcreteProductB2:  # создать велосипед
        return ConcreteProductB2()


def client_code(factory: AbstractFactory) -> None:
    """
    Клиентский код работает с фабриками и продуктами только через абстрактные
    типы: Абстрактная Фабрика и Абстрактный Продукт. Это позволяет передавать
    любой подкласс фабрики или продукта клиентскому коду, не нарушая его.
    """
    product_a = factory.create_product_a()  # создем какое-то колесо
    product_b = factory.create_product_b()  # создаем какое-то средство передвижения

    # устанавливаем на какое-то средство передвижения какое-то колесо
    print(f"{product_b.another_useful_function_b(product_a)}")
    print(f"{product_b.useful_function_b()}")  # едем


if __name__ == "__main__":
    """
    Клиентский код может работать с любым конкретным классом фабрики.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())
