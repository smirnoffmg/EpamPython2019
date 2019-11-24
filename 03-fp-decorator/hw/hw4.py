from threading import Timer


def make_cache(maxtime):
    cache = []

    def remove():
        print(cache)
        del cache[:]
        print(cache)

    def wrapper(func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            cache.append({args: result})
            return result
        t = Timer(maxtime, remove)
        t.start()
        return inner
    return wrapper


@make_cache(30)
def slow_function(n):
    if n < 2:
        return n

    return slow_function(n - 1) + slow_function(n - 2)


slow_function(1234)