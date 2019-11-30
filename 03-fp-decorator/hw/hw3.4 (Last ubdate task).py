# Написать applydecorator который работает так:


def applydecorator(func):

    def decorator(wraps):
        wraps.__name__ = func.__name__
        return wraps
    return decorator

@applydecorator
def saymyname(f, *args, **kwargs):
  print('Name is', f.__name__)
  return f(*args, **kwargs)\

@applydecorator
def andrey(f, *args, **kwargs):
  print('Name is', f.__name__)
  return f(*args, **kwargs)


@saymyname
def foo(*whatever):
    return whatever

print(*foo(40, 2), foo.__name__)


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








# >>>foo
# >>>40 2
# То есть избавляет нас от необходимости писать wrapper самим каждый раз.