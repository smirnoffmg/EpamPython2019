import datetime
from collections import namedtuple
Cache = namedtuple('Cache', ['time', 'count', 'func_name'])
cache1 = {}
cache2 = []
cache3 = {}


def make_cache(cache_name):
    def wrapper(func):
        def inner(*args, **kwargs):
            time = datetime.datetime.now()
            result = func(*args, **kwargs)
            time = datetime.datetime.now() - time
            tmp_cache = Cache(time.microseconds, 1, func.__name__)
            cache = globals()[cache_name]
            if isinstance(cache, list):
                if not len(cache):
                    cache.append(tmp_cache._asdict())

                else:
                    cache[0]['time'] += tmp_cache[0]
                    cache[0]['count'] += tmp_cache[1]
            else:
                if not len(cache):
                    cache.update(tmp_cache._asdict())
                else:
                    cache['time'] += tmp_cache[0]
                    cache['count'] += tmp_cache[1]
            return result
        return inner
    return wrapper


fib_array = [0, 1]


@make_cache('cache3')
def dp_fib(n):
    """dynamic programming method of fib sequence"""
    if n < 0:
        print("Incorrect input")
    elif n <= len(fib_array):
        return fib_array[n - 1]
    else:
        temp_fib = dp_fib(n - 1) + dp_fib(n - 2)
        fib_array.append(temp_fib)
        return temp_fib


@make_cache('cache1')
def fib_with_space_opt(n):
    """best way of fib: method with space optimization"""
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b


@make_cache('cache2')
def recursion_fib(n):
    """recursion method for fib sequence"""
    if n < 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return recursion_fib(n-1) + recursion_fib(n-2)


print(fib_with_space_opt(20), cache1)
print(recursion_fib(20), cache2)
print(dp_fib(20), cache3)