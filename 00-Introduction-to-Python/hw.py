# -*- coding: utf-8 -*-
import collections
from collections import Counter
from timeit import default_timer as timer

"""
Реализуйте метод, определяющий, является ли одна строка 
перестановкой другой. Под перестановкой понимаем любое 
изменение порядка символов. Регистр учитывается, пробелы 
являются существенными.
"""



def time_function(function: object):
    def timed(str1, str2):
        time_start = timer()
        result = function(str1, str2)
        time_stop = timer()
        print(f"\n Time of {function.__name__} is:", "{:.6} sec".format(time_stop-time_start))

        return result
    return timed


@time_function
def esy_tim_sort(str1: str, str2: str) -> bool:
    """
    Function, uses method sorted(str),
    for checking all characters in a strings
    """
    assert len(str1) == len(str2), 'Different string lengths (length str1: {0}, length str2: {1})'.format(len(str1), len(str2))
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False


with open('text1.txt', 'r') as text1, open('text2.txt', 'r') as text2:
    text1 = text1.read()
    text2 = text2.read()

assert esy_tim_sort('Aab B', 'Bb aA'), 'Strings are not permutations'
assert esy_tim_sort('a b', ' ba'), 'Strings are not permutations'
assert esy_tim_sort(text1, text2), 'Strings are not permutations'


@time_function
def collection_dict(str1: str, str2: str) -> bool:
    """
    This function uses module collections to create
    initial dict put new keys in it as characters
    and count their numbers in the str1 and str2 and subtract them
    to check for similarity
    """
    dict_counter = collections.defaultdict(int)
    for i in str1:
        dict_counter[i] += 1
    for i in str2:
        dict_counter[i] -= 1
    assert not any(dict_counter.values()), f"Look at this {dict_counter}!"
    return True


assert collection_dict('Aab B', 'B abA'), 'Strings are not permutations'
assert collection_dict('a b', ' ba'), 'Strings are not permutations'
assert collection_dict(text1, text2), 'Strings are not permutations'


@time_function
def set_conversion(str1: str, str2: str) -> bool:
    """
    Function conversions each line strings to type set() and compare them
    :param str1:
    :param str2:
    :return: bool
    """
    assert len(str1) == len(str2), f'Different string lengths (length str1: {len(str1)}, length str2: {len(str2)})'
    if set(str1) == set(str2):
        return True


assert set_conversion('Aab B', 'Bb aA'), 'Strings are not permutations'
assert set_conversion('a b', ' ba'), 'Strings are not permutations'
assert set_conversion(text1, text2), 'Strings are not permutations'


@time_function
def structure_dict(str1: str, str2: str) -> bool:
    """
    This function uses initial dict_char put new keys in it as characters
    and count their numbers in the str1 and str2 and subtract them
    to check for similarity
    """
    dict_chars = {}
    for i in str1:
        if dict_chars.get(i, None) is None:
            dict_chars[i] = 0
        dict_chars[i] += 1
    for i in str2:
        if dict_chars.get(i, None) is None:
            dict_chars[i] = 0
        dict_chars[i] -= 1

    assert not any(dict_chars.values()), "Please, attention this %s" % dict_chars
    return True


assert structure_dict('Aab B', 'Bb aA'), 'Strings are not permutations'
assert structure_dict('a b', ' ba'), 'Strings are not permutations'
assert structure_dict(text1, text2), 'Strings are not permutations'


@time_function
def count_elements(str1: str, str2: str) -> bool:
    """
    This function uses count(), which return the number of occurrences
    of i in the array.
    :param str1:
    :param str2:
    :return:
    """
    assert len(str1) == len(str2), f'Different string lengths (length str1: {len(str1)}, length str2: {len(str2)})'
    return all(str1.count(i) == str2.count(i) for i in str1)


assert count_elements('Aab B', 'Bb aA'), 'Strings are not permutations'
assert count_elements('a b', ' ba'), 'Strings are not permutations'
assert count_elements(text1, text2), 'Strings are not permutations'


@time_function
def collections_counter(str1, str2):
    one_count, two_count = Counter(str1), Counter(str2)
    assert one_count == two_count, f'Different string items(items str1: {one_count.items()},' \
                                   f' items str2: {two_count.items()})'
    return True


assert collections_counter('Aab B', 'Bb aA'), 'Strings are not permutations'
assert collections_counter('a b', ' ba'), 'Strings are not permutations'
assert collections_counter(text1, text2), 'Strings are not permutations'


