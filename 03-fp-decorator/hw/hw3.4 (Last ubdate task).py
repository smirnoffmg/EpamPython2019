# Написать applydecorator который работает так:

def applydecorator(name):

    def wrapper(*args):
        func(args)
    return wrapper

@applydecorator
def saymyname(f, *args, **kwargs):
    print('Name is', f.__name__)
    return f(*args, **kwargs)

# @saymyname

def foo(*whatever):
    return whatever

print(*foo(1,2,3))

# saymyname(*foo(1,2,3))
#
#
# def decorator_function(func):
#     def wrapper():
#         print('Функция-обёртка!')
#         print('Оборачиваемая функция: {}'.format(func))
#         print('Выполняем обёрнутую функцию...')
#         wrapper
#         print('Выходим из обёртки')
#     return func
#
# @decorator_function
# def hello_world():
#     return "Hello world"
#
# print(hello_world())
#
# @hello_world
# def goodby_world():
#     print("goodby_world")

