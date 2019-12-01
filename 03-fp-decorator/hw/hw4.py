def applydecorator(prev_dec):
    def wrapper(func):
        def func_caller(*args, **kwargs):
            return func(*args, **kwargs)
        return func_caller
    return wrapper


@applydecorator
def saymyname(f, *args, **kwargs):
    print('Name is', f.__name__)
    print(f(*args, **kwargs))
    return f(*args, **kwargs)


# saymyname is now a decorator
@saymyname
def foo(*whatever):
    return whatever


print(*(foo(40, 2)))
