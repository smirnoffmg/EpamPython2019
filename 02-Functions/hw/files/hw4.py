import inspect


def modified_func(func, *fixated_args, **fixated_kwargs):
    def new_func(*fixed_args, **fixed_kwargs):
        fixed_args = (*fixated_args, *fixed_args)
        fixed_kwargs = {**fixated_kwargs, **fixed_kwargs}
        func(*fixed_args, **fixed_kwargs)
        new_func.__name__ = f'func_{func.__name__}'
        new_func.__doc__ = f"""A func implementation of {func.__name__}
        with pre-applied arguments being:
        {fixated_args}, {fixated_kwargs}
        source_code:
        {inspect.getsource(func)}"""
    return new_func
