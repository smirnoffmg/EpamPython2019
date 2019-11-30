

def applydecorator(func):
    def inner(f, *args, **kwargs):
        func(f, *args, *kwargs)
        return f
    return inner


@applydecorator
def saymyname(f, *args, **kwargs):
    print('Name is', f.__name__)
    return f(*args, **kwargs)


@saymyname
def foo(*whatever):
    return whatever

print(*foo(40, 2))

