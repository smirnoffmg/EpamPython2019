# -*- coding: utf-8 -*-

"""
Реализуйте метод, определяющий, является ли одна строка 
перестановкой другой. Под перестановкой понимаем любое 
изменение порядка символов. Регистр учитывается, пробелы 
являются существенными.
"""

def is_permutation(a: str, b: str) -> bool:
    return sorted(a) == sorted(b)


assert is_permutation('baba', 'abab')
assert is_permutation('abbba', 'abab')
