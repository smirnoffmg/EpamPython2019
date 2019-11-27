Написать applydecorator который работает так:


```python

@applydecorator
def saymyname(f, *args, **kwargs):
  print('Name is', f.__name__)
  return f(*args, **kwargs)

# saymyname is now a decorator
@saymyname
def foo(*whatever):
    return whatever

print(*(foo(40, 2)))
>>>foo
>>>40 2
```

То есть избавляет нас от необходимости писать wrapper самим каждый раз.