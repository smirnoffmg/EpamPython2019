import string

"""
hw1
"""


def letters_range(first_arg: str, *args, **kw) -> list:
    """Return an object that produces a sequence of letter from start (inclusive)

    The letters_range function, takes for start and stop,
    the letters of the Latin alphabet (takes an integer as step)
    and returns a list of letters, starting with the one specified
    as start (or starting with 'a' if start is not specified),
    to the one specified as stop in increments of step (default is 1).
    Also, it is possible to accept a dictionary with replacements for
    letters similar to transliteration.
    """
    len_arguments = len((first_arg,) + args)
    if len_arguments > 3:
        raise TypeError("{function} takes 3 positional arguments but {parametrs} "
                        "were given".format(function=letters_range.__name__, parametrs=len_arguments))
    elif len(args):
        start = string.ascii_letters.index(first_arg)
        stop = string.ascii_letters.index(args[0])
    else:
        start = string.ascii_letters.index('a')
        stop = string.ascii_letters.index(first_arg)
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


"""
hw2
"""


def atom(arg=None):
    """Returns 3 functions to work with the value of argument -
    get_value, set_value, process_value, delete_value.


    About nested functions:
    get_value - allows you to get the value of the stored variable;

    set_value - allows you to set a new value for the stored variable
    and returns it;

    process_value - takes as many functions as arguments and sequentially
    (in the order of enumeration of the arguments) applies these functions
    to the stored variable, updating its value and returning the resulting
    total value;

    delete_value - deletes a value.
    """

    val = arg
    massage = """
    Variable 'val' has been deleted already.
    Assign a new value to the set_value
    method before attempting to delete
    """

    def get_value():
        nonlocal val
        try:
            return val
        except NameError:
            raise NameError(massage)

    def set_value(new_val=None):
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


# get_value, set_value, process_value, delete_value = atom()
# print("is run", get_value())
# print("set is run", set_value(2))
# print("get is run", get_value())
# print("delet is run", delete_value())
# print("set is run", set_value(3))
# print("get is run", get_value())
# func = [lambda x: x, lambda x: x+1, lambda x: x*x]
# print("process is run", process_value(*func))
# print("get is run", get_value())


"""
hw3
"""


def make_it_count(function, name_global_var):
    """Function increments

    Returning a new function, with behavior as func and
    increments the value of a global variable called
    counter_name every function call.
    """
    def inner():
        res = function
        globals()[name_global_var] = globals().get(name_global_var, 0) + 1
        return res, "Increment of {}".format(name_global_var), globals()[name_global_var]

    return inner()


def f():
    return "{}".format(f.__name__)


print(make_it_count(f, "hw1"))
print(make_it_count(f, "hw1"))
print(make_it_count(f, "hw2"))
print(make_it_count(f, "hw2"))
print(make_it_count(f, "hw3"))


"""
hw4
"""


# partial
def modified_func(my_func, *fixated_args, **fixated_kw):
    """Returns a function with the same behavior as a function
    my_func that is called using fixated_args and fixated_kwargs

    When called with new positional *args and named **kw arguments,
    ascribes new positional and overrides or supplements the values
    of named arguments
    """

    def inner(*args, **kw):
        if args:
            f_args = fixated_args + args
        else:
            f_args = fixated_args
        kw.update(fixated_kw)

        return my_func(*f_args, **kw)

    func_documentation = """
    A func implementation of {0}
    with pre-applied arguments being:
    {args} and {kw} source_code:
    """.format(my_func.__name__, args=fixated_args, kw=fixated_kw)

    inner.__doc__ = func_documentation
    inner.__name__ = my_func.__name__

    return inner


def test(*args, **kw):
    return "Я функция {name}, которая приняла\nпозиционные аргументы: {0} и" \
           "\nименованные аргументы: {1}!".format(args, kw, name=test.__name__)


fix_args = (4,5)
fix_kw = {"a": 3, "d": 4}
args = (1, 2, 3)
kw = {"a": 1, "b": 2}
print(modified_func(test, *fix_args, **fix_kw)(*args, **kw))
print(modified_func(test, *fix_args, **fix_kw).__doc__)
print(modified_func(test, *fix_args, **fix_kw).__name__)
