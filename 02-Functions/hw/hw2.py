str_of_letters = 'abcdefghijklmnopqrstuvwxyz'
list_of_letters = [i for i in str_of_letters]
# print(list_of_letters)

ran = range(10, 12)


def letters_range(stop, start=1, step=2):
    pass


# print ("""Generates the characters from `a` to `z`, inclusive.""")
# def character_range(char1, char2):
#     for char in range(ord(char1), ord(char2 ) +1):
#         yield (char)
#
# for letter in character_range('a', 'z'):
#     print( chr(letter), end=", " )

import string


def letters_range(arg, *args, **kw):
    """

    """
    len_arguments = len((arg,) + args)
    if len_arguments > 3:
        raise TypeError("{function} takes 3 positional arguments but {parametrs} "
                        "were given".format(function=letters_range.__name__, parametrs=len_arguments))
    elif len(args):
        start = string.ascii_letters.index(arg)
        stop = string.ascii_letters.index(args[0])
    else:
        start = string.ascii_letters.index('a')
        stop = string.ascii_letters.index(arg)
    step = 1 if len(args) < 2 else args[1]

    for i in string.ascii_letters[start:stop:step]:
        if i in kw:
            yield kw[i]
        else:
            yield i


# print([i for i in letters_range('b', 'w', 2)])
# print([i for i in letters_range('g')])
# print([i for i in letters_range('g', 'p')])
# print([i for i in letters_range('g', 'p', **{'l': 7, 'o': 0})])
# print([i for i in letters_range('p', 'g', -2)])
# print([i for i in letters_range('a')])


def atom(arg=None):
    """

    :param arg:
    :return:
    """

    val = arg
    print(val)

    def get_value():
        nonlocal val
        return val

    def set_value(new_val):
        nonlocal val
        val = new_val
        return val

    def delete_value():
        nonlocal val
        del val

    def process_value(*func):
        nonlocal val
        for i in func:
            val = i(val)
        return val

    return get_value, set_value, process_value, delete_value


# get_value, set_value, process_value, delete_value = atom(1)
# print(get_value())
# print(set_value(2))
# print(get_value())
# print(delete_value())
# print(set_value(3))
# print(get_value())
# func = [lambda x: x, lambda x: x+1, lambda x: x*x]
# print(process_value(*func))
# print(get_value())


def make_it_count(func, name_global_var, global_dict={}):
    def inner():
        if name_global_var not in global_dict:
            global_dict[name_global_var] = 0
        res = func
        global_dict[name_global_var] += 1
        globals().update(global_dict)
        print(global_dict)
        return res
    return inner

def f():
    return "{}".format(f.__name__)

# f = f
# print(make_it_count(f, "hw1")()())
# print(make_it_count(f, "hw1")())
# print(make_it_count(f, "hw1")())
# print(make_it_count(f, "hw2")())
# print(make_it_count(f, "hw2")())
# print(make_it_count(f, "hw3")())
# print(globals()['hw2'])


def modified_func(func, *args, **kw):
    """

    :param func:
    :param fixed_args:
    :param fixed_kw:
    :return:
    """
    def inner():
        print("args", args)
        print("kw", kw)

        if args and kw:
            print("Yes")
            fix_arg = args
            fix_kw = kw
            return f(*(args+fix_arg), **(kw.update(kw)))
        else:
            print("No")
            return f

    inner.__doc__ = """
                    A func implementation of {0}
                    with pre-applied arguments being:
                    <перечисление имен и значений fixated_args и fixated_kwargs>
                    source_code:
                    """.format(func.__name__)
    return inner

def f(*args, **kw):
    return args, kw

print(modified_func(f, *(1,2), **{"a":1, "b":2}))
print(modified_func(f))

new_f1 = modified_func(f, *(1, 2), **{"a": 1, "b": 2})
new_f2 = modified_func(f)

# print("f1", new_f1(*(3,), **{"c":3}))
print("f1", new_f1())
print("f2", new_f2())