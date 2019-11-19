global_value = 0


def make_it_count(func, counter_name):

    def new_func():
        globals()[counter_name] += 1
        func()

    return new_func