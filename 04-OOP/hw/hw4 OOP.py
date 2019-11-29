import datetime
from dataclasses import dataclass
from typing import NamedTuple


class Teacher(NamedTuple):
    last_name: str
    first_name: str

    @staticmethod
    def create_hw(text, days) -> object:
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
    student.first_name  # Petrov

    expired_homework = teacher.create_hw('Learn functions', 3.2)
    expired_homework.created  # Example: 2019-05-26 16:44:30.688762
    expired_homework.deadline  # 0:00:00
    expired_homework.text  # 'Learn functions'

    # create function from method and use it
    create_homework_too = teacher.create_hw
    oop_homework = create_homework_too('create 2 simple classes', 5)
    oop_homework.deadline  # 5 days, 0:00:00
    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late
