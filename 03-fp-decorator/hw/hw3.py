import math
import time
from functools import wraps, reduce


# """
# hw1
# """
#
#
# """Problem 6"""
# n = 100
# p6 = sum([i for i in range(1, n + 1)]) ** 2 - sum([i ** 2 for i in range(1, n + 1)])
# print(p6)
#
#
# """ Problem 9. Introduction
# Because of the ratio of a, b, c in a Pythagorean triplet no variable can ever be
# larger than half the sum of a + b + c therefore I have lowered the upper limit to 500 or sum_elements // 2 """
#
# sum_elements = 1000
# half_sum = sum_elements // 2
# p9 = [(a, b, 1000 - (a + b)) for a in range(1, half_sum) for b in range(a + 1, half_sum) if
#       a ** 2 + b ** 2 == (sum_elements - (a + b)) ** 2]
# print("a = {0}, b = {1}, c = {2}".format(*p9[0]))
#
#
# """Problem 40"""
# N = 10**6
# p40 = reduce(lambda x, y: x*y, [int(list("".join(str(i) for i in range(1, N + 1)))[x-1])
#                                for x in [10**i for i in range(7)]])
#
# print("The value of the following expression is {}".format(p40))
#
#
# """Problem 48"""
# p48 = [i ** i for i in range(1, 1001)][-1:-11:-1]
# print("Last {len_last_list_elements} elements is {value}\n".format(len_last_list_elements=len(p48),
#                                                              value=p48))
#
# """
# hw2
# """
#
#
# def return_armstrong_true_or_not(pass_number: int) -> bool:
#     """Function determines the Armstrong number in functional form
#     and return result - True or False
#
#     Armstrong's number is a natural number, which in a given number
#     system is equal to the sum of its digits raised to a power equal
#     to the number of its digits.
#     """
#
#     result = reduce(lambda x, y: x + pow(int(y), len(str(pass_number))),
#                     str(pass_number), 0)
#     if pass_number == result:
#         return pass_number
#
#
# number = 153
# assert return_armstrong_true_or_not(number) == number, "The number {} is not an Armstrong number".format(number)
#
#
# """
# hw3
# """
#
#
# def return_collatz_count_steps(pass_number: int, count=0) -> int:
#     """Calculate count of number steps to satisfy the condition:
#     number == 1
#
#     collatz() that has one parameter named number.
#     If number is even, then collatz() should print
#     number // 2 and return this value. If number is
#     odd, then collatz() should print and return 3 * number + 1.
#     """
#     try:
#         pass_number = int(pass_number)
#     except ValueError:
#         print("Please enter a number correct!")
#     else:
#         if pass_number == 1:
#             return count
#         elif pass_number % 2 == 0:
#             count += 1
#             return return_collatz_count_steps(pass_number // 2, count=count)
#         else:
#             count += 1
#             return return_collatz_count_steps(3 * pass_number + 1, count=count)
#
#
# assert int(return_collatz_count_steps(2)) == 1
# assert return_collatz_count_steps(12) == 9
# assert return_collatz_count_steps(1000000) == 152
#
#
# """
# hw4
# """
#
#
# def make_cache_with_arg_version1(decorator_time=3):
#     """Stores the result of the function over time time_live
#
#     Saves the results of previous function calls in its
#     storage for a certain time, which is passed as an
#     argument to the decorator"""
#
#     def decorator(func):
#         #  I am a cache and I will be created at the time of decorating the function
#         storage_function_value = {}
#         @wraps(func)
#         def inner(*args, **kwargs):
#             try:
#                 time_is_over = time.monotonic() - storage_function_value[args][-1] > decorator_time
#             except KeyError:
#                 create_cache = list(func(*args, **kwargs))
#                 create_cache.append(time.monotonic())
#                 storage_function_value[args] = create_cache
#                 return create_cache, "New, just created cache"
#             else:
#                 if not time_is_over:
#                     return storage_function_value[args], "From cache"
#                 else:
#                     new_cache_value = list(func(*args, **kwargs))
#                     new_cache_value.append(time.monotonic())
#                     storage_function_value[args] = new_cache_value
#                     return new_cache_value, "New, with cache replacement"
#         return inner
#     return decorator
#
#
# @make_cache_with_arg_version1(3)
# def slow_func(*args):
#     for value in args:
#         yield value.upper()
#
# # print("make_cache_with_arg_version1")
# # print(slow_func("one"))
# # time.sleep(1)
# # print(slow_func("three"))
# # print(slow_func("one"))
# # time.sleep(4)
# # print(slow_func("three"))
#
#
# def make_cache_with_arg_version2(decorator_time=3):
#     """Stores the result of the function over time time_live
#
#     Saves the results of previous function calls in its
#     storage for a certain time, which is passed as an
#     argument to the decorator"""
#
#
#     def decorator(func):
#         #  I am a cache and I will be called only once when you ask me to create a decorator for you.
#         storage_function_value = {}  # {args: [result, time]}
#         @wraps(func)
#         def inner(*args, **kwargs):
#             if args in storage_function_value and \
#                     time.monotonic() - storage_function_value[args][-1] < decorator_time:
#                 return storage_function_value[args], "From cache"
#             create_cache = list(func(*args, **kwargs))
#             create_cache.append(time.monotonic())
#             storage_function_value[args] = create_cache
#             return create_cache, "New created cache"
#
#         return inner
#     return decorator
#
#
# @make_cache_with_arg_version2(3)
# def slow_func(*args):
#     for value in args:
#         yield value.upper()

# print("make_cache_with_arg_version2")
# print(slow_func("one"))
# time.sleep(1)
# print(slow_func("three"))
# print(slow_func("one"))
# time.sleep(4)
# print(slow_func("three"))


"""
hw4  applydecorator
"""

# def applydecorator(wraps
#                    ):
#     def decorator(wraps):
#         wraps.__name__ = func.__name__
#         wraps.__doc__ = func.__doc__
#         wraps.__original_func = func
#         return wraps
#     return decorator

# @applydecorator
# def saymyname(f, *args, **kwargs):
#   print('Name is', f.__name__)
#   return f(*args, **kwargs)

# @saymyname
# def foo(*whatever):
#     return whatever

# print(*(foo(40, 2)))


def decorator_maker():
    print("Я создаю декораторы! Я буду вызван только раз: "
          "когда ты попросишь меня создать тебе декоратор.")

    def my_decorator(func):
        print("Я - декоратор! Я буду вызван только раз: в момент декорирования функции.")

        def wrapped():
            print("Я - обёртка вокруг декорируемой функции. "
                  "Я буду вызвана каждый раз когда ты вызываешь декорируемую функцию. "
                  "Я возвращаю результат работы декорируемой функции.")
            return func()

        print("Я возвращаю обёрнутую функцию.")

        return wrapped

    print("Я возвращаю декоратор.")
    return my_decorator


"""
hw5
"""


def counter_stopwatch(g_name_count, g_name_time):

    #  This is the creator of decorators, it will be called only once:
    #  "when you call a decorator."
    def actual_decorator(func):
        """
        Decorator that reads and displays the number of calls
        to the function being decorated.
        """
        # This is actual_decorator, it will be called only once:
        # at the time of decorating the function
        @wraps(func)
        def wrapper(*args, **kwargs):
            # This is wrapper, it will be called every time you call
            # a decorated function.
            wrapper.count = wrapper.count + 1
            start = time.perf_counter()
            res = func(*args, **kwargs)
            wrapper.function_work_time = wrapper.function_work_time \
                                         + time.perf_counter() - start
            globals()[g_name_count] = wrapper.count
            globals()[g_name_time] = wrapper.function_work_time
            return res
        wrapper.count = 0
        wrapper.function_work_time = 0
        return wrapper
    return actual_decorator


g_count = "fib_dinamic_count"
g_time = "fib_dinamic_time"


@counter_stopwatch(g_count, g_time)
def fib_dinamic_programin_approach(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


fib_dinamic_programin_approach(500)
fib_dinamic_programin_approach(500)
print("count", globals()[g_count], "time", globals()[g_time])

g_count = "fib_closed_form_expression_count"
g_time = "fib_closed_form_expression_time"


@counter_stopwatch(g_count, g_time)
def fib_closed_form_expression(n):
    """
    <a href = http://en.wikipedia.org/wiki/Fibonacci_number#Closed-form_expression>Closed form expression</a>
    """
    sqrt_5 = math.sqrt(5)
    phib = (sqrt_5 + 1) / 2
    return int(phib ** n / sqrt_5 + 0.5)


fib_closed_form_expression(500)
fib_closed_form_expression(500)
print("count", globals()[g_count], "time", globals()[g_time])

g_count = "fib_recursion_count"
g_time = "fib_recursion_time"


@counter_stopwatch(g_count, g_time)
def fib_recursion(n):
    if n < 3:
        return 1
    return fib_recursion(n - 1) + fib_recursion(n - 2)


fib_recursion(2)
print(fib_recursion(1))
print("count", globals()[g_count], "time", globals()[g_time])




fib_list = [fib_closed_form_expression]







