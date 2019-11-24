from functools import reduce

n = 100
p6 = sum([i for i in range(1, n + 1)]) ** 2 - sum([i ** 2 for i in range(1, n + 1)])
print(p6)

""" Because of the ratio of a, b, c in a Pythagorean triplet no variable can ever be
 larger than half the sum of a + b + c therefore I have lowered the upper limit to 500 or sum_elements // 2 """

sum_elements = 1000
half_sum = sum_elements // 2
p9 = [(a, b, 1000 - (a + b)) for a in range(1, half_sum) for b in range(a + 1, half_sum) if
      a ** 2 + b ** 2 == (sum_elements - (a + b)) ** 2]
print("a = {0}, b = {1}, c = {2}".format(*p9[0]))

N = 10*6
p40 = reduce(lambda x, y: x*y, [int(list("".join(str(i) for i in range(1, N + 1)))[x-1])
                               for x in [10**i for i in range(7)]])
print(p40)


p48 = [i ** i for i in range(1, 1001)][-1:-11:-1]
print(p48)


def return_armstrong_true_or_not(number: int) -> bool:
    """Function determines the Armstrong number in functional form
    and return result - True or False

    Armstrong's number is a natural number, which in a given number
    system is equal to the sum of its digits raised to a power equal
    to the number of its digits.
    """

    result = reduce(lambda x, y: x + pow(int(y), len(str(number))),
                    str(number), 0)
    if number == result:
        return number


number = 153
assert return_armstrong_true_or_not(number) == number


def return_collatz_count_steps(number: int, count=None) -> int:
    """Calculate the number of steps for count

    collatz() that has one parameter named number.
    If number is even, then collatz() should print
    number // 2 and return this value. If number is
    odd, then collatz() should print and return 3 * number + 1.
    """
    if count is None:
        count = 0
    try:
        number = int(number)
    except ValueError:
        print("Please enter a number correct!")
    else:
        if number == 1:
            return count
        elif number % 2 == 0:
            count += 1
            return return_collatz_count_steps(number // 2, count=count)
        else:
            count += 1
            return return_collatz_count_steps(3 * number + 1, count=count)


assert int(return_collatz_count_steps(2)) == 1
assert return_collatz_count_steps(12) == 9
assert return_collatz_count_steps(1000000) == 152

import time as t

# def make_cache_with_arg(decorator_time):
#     print("make_cache_with_arg", decorator_time)
#     def my_decorator(func):
#         print("my_decorator", decorator_time)
#         def wrapper(*args, **kw):
#             print("wrapper", decorator_time)
#             return func(*args, **kw)
#         return wrapper
#     return my_decorator


# @make_cache_with_arg(3)
# def slow_function():
#     pass

# slow_function()
