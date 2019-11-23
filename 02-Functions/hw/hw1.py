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


