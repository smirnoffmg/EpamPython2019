import functools


def saver(func):
    def decorator(wraps):
        wraps.__name__ = func.__name__
        wraps.__doc__ = func.__doc__
        wraps.__original_func = func
        return wraps
    return decorator


def print_result(func):
    @saver(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        return result
    return wrapper


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


if __name__ == '__main__':
    custom_sum([1, 2, 3], [4, 5])
    custom_sum(1, 2, 3, 4)
    without_print = custom_sum.__original_func
    # the result returns without printing
    without_print(1, 2, 3, 4)

