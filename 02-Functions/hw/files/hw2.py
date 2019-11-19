def atom(value=None):

    def get_value():
        return value

    def set_value(new_value):
        nonlocal value
        value = new_value
        return value

    def process_value(*funcs):
        nonlocal value
        for func in funcs:
            value = func(value)
        return value

    def delete_value():
        nonlocal value
        del value

    return get_value, set_value, process_value, delete_value
