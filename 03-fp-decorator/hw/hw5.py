import datetime

cache = {}


def make_cache(cache):
    def wrapper(func):
        def inner(*args, **kwargs):
            time = datetime.datetime.now()
            result = func(*args, **kwargs)
            time = datetime.datetime.now() - time
            if not len(cache):
                cache['time'] = time.microseconds
                cache['count'] = 1
            else:
                cache['time'] += time
                cache['count'] += 1
            return result
        return inner
    return wrapper


FibArray = [0,1]


@make_cache(cache)
def fib(n):
    """best way of fib: method with using DP and space optimization"""
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

print(fib(123), cache, sep='\n')