import inspect
import hw2


def modified_func(func, *fixated_args, **fixated_kwargs):
    def new_func(*fixed_args, **fixed_kwargs):
        """A func implementation of {func_name}
        with pre-applied arguments being:
        fixated_args: {fixated_args},
        fixated_kwargs: {fixated_kwargs}
        source_code:
        {source}"""
        fixed_args = (*fixated_args, *fixed_args)
        fixed_kwargs = {**fixated_kwargs, **fixed_kwargs}
        new_func.__name__ = func.__name__
        params = inspect.signature(func).parameters
        pos_args = list(fixated_args)
        for i, (name, param) in enumerate(params.items()):
            if str(param).find('=') != -1:
                fixated_kwargs.update({name: pos_args[i]})
                pos_args.remove(pos_args[i])
        new_func.__doc__ = new_func.__doc__.replace('{source}', inspect.getsource(func))
        new_func.__doc__ = new_func.__doc__.replace('{func_name}', new_func.__name__)
        new_func.__doc__ = new_func.__doc__.replace('{fixated_args}', str(pos_args))
        new_func.__doc__ = new_func.__doc__.replace('{fixated_kwargs}', str(fixated_kwargs))
        return func(*fixed_args, **fixed_kwargs)
    return new_func


def print_args(*args, **kwargs):
    print(*args, kwargs)


test = modified_func(print_args, 'arg', **{'l': 7, 'o': 0})
test('new_arg', new_kwarg='777')
print(test.__name__)
print(test.__doc__)

test_atom = modified_func(hw2.atom, 1)
print(test_atom()[0]())
print(test_atom.__doc__)

test_any = modified_func(any, [1, 2])
#нельзя получить исходный код built-in функций
#т.к getsource может показать только Python код
#а они написаны на C
# test_any()
# print(test_any.__doc__)


