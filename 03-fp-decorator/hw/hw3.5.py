import math
import time
from functools import wraps


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


g_count = "fib_recursion_count"
g_time = "fib_recursion_time"


@counter_stopwatch(g_count, g_time)
def fib_recursion(n):
    if n < 3:
        return 1
    return fib_recursion(n - 1) + fib_recursion(n - 2)


g_count = "fib_no_recursion_count"
g_time = "fib_no_recursion_time"


@counter_stopwatch(g_count, g_time)
def fib_no_recursion(n):
    a, b = 1, 1
    i = 2
    while i < n:
        fib_sum = a + b
        a = b
        b = fib_sum
        i += 1
    return fib_sum


g_count = "fib_memoriz_count"
g_time = "fib_memoiz_time"
memory = {0: 0, 1: 1}


@counter_stopwatch(g_count, g_time)
def fib_memoiz(n):
    global memory
    if n in memory:
        return memory[n]
    memory[n] = fib_memoiz(n - 1) + fib_memoiz(n -2)
    return memory[n]


list_functions = [fib_dinamic_programin_approach, fib_closed_form_expression,
                  fib_recursion, fib_no_recursion, fib_memoiz]

list_name_for_global_var = [("fib_dinamic_count", "fib_dinamic_time"),
                            ("fib_closed_form_expression_count", "fib_closed_form_expression_time"),
                            ("fib_recursion_count", "fib_recursion_time"),
                            ("fib_no_recursion_count", "fib_no_recursion_time"),
                            ("fib_memoriz_count", "fib_memoiz_time")]
times = []
for i, func in enumerate(list_functions):
    for j in range(5, 25, 2):
        func(j)
    times.append(globals()[list_name_for_global_var[i][1]])
    print(func.__name__, f"\ncall of count: {globals()[list_name_for_global_var[i][0]]},"
                         f"\ntime: {globals()[list_name_for_global_var[i][1]]}")

work_algorithms_sorted_by_speed = sorted(list(zip([func.__name__ for func in list_functions], times)),
                                         key=lambda x: x[1])

print("Самый быстрый алгоритм: ", work_algorithms_sorted_by_speed[0])
