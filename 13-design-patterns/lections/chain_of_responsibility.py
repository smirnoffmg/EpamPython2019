from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    Интерфейс Обработчика объявляет метод построения цепочки обработчиков. Он
    также объявляет метод для выполнения запроса.
    """

    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    Поведение цепочки по умолчанию может быть реализовано внутри базового класса
    обработчика.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Возврат обработчика отсюда позволит связать обработчики простым
        # способом, вот так:
        # handler1.set_next(handler2).set_next(handler3)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


"""
Все Конкретные Обработчики либо обрабатывают запрос, либо передают его
следующему обработчику в цепочке.
"""

MAX_FUEL_LEVEL = 100
MAX_OIL_LEVEL = 100


class Car:
    def __init__(self, fuel_level=100, wheels_broken=0, oil_level=100, brake_correct=True):
        self._fuel_level = fuel_level  # 0 - 100 %
        self._wheels_broken = wheels_broken  # 0 - 4
        self._oil_level = oil_level  # 0 - 100 %
        self._brake_correct = brake_correct  # True or False

    def add_fuel(self, fuel_num):
        self._fuel_level += fuel_num

    def add_oil(self, oil_num):
        self._oil_level += oil_num


class FuelHandler(AbstractHandler):
    def handle(self, car: Car):
        if car._fuel_level < MAX_FUEL_LEVEL:
            fuel_to_add = MAX_FUEL_LEVEL - car._fuel_level
            car.add_fuel(fuel_to_add)
            print(f"Долито {fuel_to_add} топлива в бак")
        if self._next_handler:
            return self._next_handler.handle(car)


class WheelHandler(AbstractHandler):
    def handle(self, car: Car):
        if car._wheels_broken > 0:
            print(f"Смена колёс: {car._wheels_broken} шт.")
            car._wheels_broken = 0
        if self._next_handler:
            return self._next_handler.handle(car)


class OilHandler(AbstractHandler):
    def handle(self, car: Car):
        if car._oil_level < MAX_OIL_LEVEL:
            oil_to_add = MAX_OIL_LEVEL - car._oil_level
            car.add_oil(oil_to_add)
            print(f"Долито {oil_to_add} масла")
        if self._next_handler:
            return self._next_handler.handle(car)


class BrakeHandler(AbstractHandler):
    def handle(self, car: Car):
        if not car._brake_correct:
            print("Починка тормозов")
            car._brake_correct = True
        if self._next_handler:
            return self._next_handler.handle(car)


def repair_car(car):
    fuel_handler = FuelHandler()
    wheel_handler = WheelHandler()
    oil_handler = OilHandler()
    brake_handler = BrakeHandler()

    fuel_handler.set_next(wheel_handler).set_next(oil_handler).set_next(brake_handler)

    fuel_handler.handle(car)


car_to_service = Car(fuel_level=25, wheels_broken=2, oil_level=10, brake_correct=False)
repair_car(car_to_service)
