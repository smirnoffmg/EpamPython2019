"""
Написать applydecorator который работает так, что избавляет нас от
необходимости писать wrapper самим каждый раз.
"""
import sys
from io import StringIO



@applydecorator
def saymyname(f, *args, **kwargs):
  print('Name is', f.__name__)
  return f(*args, **kwargs)

# saymyname is now a decorator
@saymyname
def foo(*whatever):
    return whatever


if __name__ == '__main__':
    sys.stdout = StringIO()
    foo(40, 2)
    assert sys.stdout.getvalue() == 'Name is foo\n'
