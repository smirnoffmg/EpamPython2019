import datetime


class Teacher:

    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def create_homework(text, days):

        return HomeWork(text, days)



class Student:

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def do_homework(hw: object):

        return hw if hw.is_active() else print("You are late") and None


class HomeWork:
    
    def __init__(self, text_task: str, count_days: int):
        self.text = text_task
        self.deadline = datetime.timedelta(count_days)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:

        time_is_over = datetime.datetime.now() - self.created \
                       > self.deadline
        return time_is_over


if __name__ == '__main__':
    teacher = Teacher('Daniil', 'Shadrin')
    student = Student('Roman', 'Petrov')
    print(teacher.last_name)  # Daniil
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






