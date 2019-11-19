def letters_range(start, stop=None, step=1, **kwargs):
    if stop is None:
        stop = start
        start = 'a'
    alphabet = [chr(i) for i in range(ord(start), ord(stop), step)]
    if kwargs:
        for key, value in kwargs.items():
            for n, i in enumerate(alphabet):
                if key == i:
                    alphabet[n] = value

    return alphabet
