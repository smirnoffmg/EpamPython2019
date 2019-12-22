# Decorator design pattern (OOP)
# https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_decorator.htm
# https://refactoring.guru/design-patterns/decorator/python/example#lang-features

# Decoration of a function (functional programming)
# https://realpython.com/primer-on-python-decorators/
# https://hackernoon.com/decorators-in-python-8fd0dce93c08

from abc import ABC, abstractmethod


class AbstractCoffee(ABC):
    """
    Базовый интерфейс Компонента определяет поведение, которое изменяется декораторами.
    """
    def __str__(self):
        return f'Coffee {hex(id(self))}; cost: {self.get_cost()}; ' \
            f'ingredients: {self.get_ingredients()}; tax: {self.get_tax()}'

    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_ingredients(self):
        pass

    def get_tax(self):
        return 0.1 * self.get_cost()


class ConcreteCoffee(AbstractCoffee):
    """
    Конкретный Компонент предоставляет реализацию поведения по умолчанию.
    Может быть несколько вариаций этих классов.
    """
    def get_cost(self):
        return 1

    def get_ingredients(self):
        return 'coffee'


class AbstractCoffeeDecorator(AbstractCoffee):
    """
    Базовый класс Декоратора следует тому же интерфейсу, что и другие
    компоненты. Основная цель этого класса - определить интерфейс обёртки для
    всех конкретных декораторов. Реализация кода обёртки по умолчанию может
    включать в себя поле для хранения завёрнутого компонента и средства его
    инициализации.
    """
    def __init__(self, decorated_coffee):
        self.decorated_coffee = decorated_coffee

    def get_cost(self):
        return self.decorated_coffee.get_cost()

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients()


class Sugar(AbstractCoffeeDecorator):
    """
    Конкретные Декораторы вызывают обёрнутый объект и изменяют его результат
    некоторым образом.
    """
    def __init__(self, decorated_coffee):
        super(Sugar, self).__init__(decorated_coffee)

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ', sugar'


class Milk(AbstractCoffeeDecorator):
    def __init__(self, decorated_coffee):
        super(Milk, self).__init__(decorated_coffee)

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 0.25

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ', milk'


class Vanilla(AbstractCoffeeDecorator):
    def __init__(self, decorated_coffee):
        super(Vanilla, self).__init__(decorated_coffee)

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 0.75

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ', vanilla'


if __name__ == '__main__':
    print('It\'s a coffee shop')
    coffee = ConcreteCoffee()
    print(coffee)

    coffee = Milk(coffee)
    print(coffee)

    coffee = Vanilla(coffee)
    print(coffee)

    coffee = Sugar(coffee)
    print(coffee)

    print('-' * 50)

    # -----------------------------------------------------------------------
    # decorator of a function
    def welcome_message(func):
        def print_wrapper(*args):
            print('Thank you for visiting our Coffee Shop!')
            func(*args)
            print('See you next time!')
        return print_wrapper

    # long form
    def print_coffee(_coffee):
        print(f'You ordered: {_coffee.get_ingredients()}; \n'
              f'The total price is: {_coffee.get_cost() + _coffee.get_tax()}$')
    decorated_print = welcome_message(print_coffee)
    decorated_print(coffee)

    print('-' * 50)

    # short form
    @welcome_message
    def decorated_print_coffee(_coffee):
        print(f'You ordered: {_coffee.get_ingredients()}; \n'
              f'The total price is: {_coffee.get_cost() + _coffee.get_tax()}$')
    decorated_print_coffee(coffee)
