"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime

1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истело ли время на выполнение задания,
    возвращает boolean

2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None

3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.

PEP8 соблюдать строго, проверку делаю автотестами и просмотром кода.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from dataclasses import dataclass
from typing import NamedTuple


class Teacher(NamedTuple):
    last_name: str
    first_name: str

    @staticmethod
    def create_homework(text, days) -> object:
        return HomeWork(text, days)


class HomeWork:

    def __init__(self, text_task: str, count_days: int):
        self.text = text_task
        self.deadline = datetime.timedelta(count_days)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        time_is_over = datetime.datetime.now() - self.created \
                       > self.deadline
        return time_is_over


@dataclass(frozen=True)
class Student:
    """
    has two fields: first and last name
    has method do_homework: it takes a Homework object and returns it,
    if the task has already expired, it prints 'You are late'
    and returns None
    """

    __slots__ = ["last_name", "first_name"]

    last_name: str
    first_name: str

    @staticmethod
    def do_homework(hw: object):
        if not hw.is_active():
            return hw


if __name__ == '__main__':
    teacher = Teacher('Daniil', 'Shadrin')
    student = Student('Roman', 'Petrov')
    teacher.last_name  # Daniil
    student.first_name  # Petrov

    expired_homework = teacher.create_homework('Learn functions', 0)
    expired_homework.created  # Example: 2019-05-26 16:44:30.688762
    expired_homework.deadline  # 0:00:00
    expired_homework.text  # 'Learn functions'

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    oop_homework.deadline  # 5 days, 0:00:00

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late
