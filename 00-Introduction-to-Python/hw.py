# -*- coding: utf-8 -*-

"""
Реализуйте метод, определяющий, является ли одна строка 
перестановкой другой. Под перестановкой понимаем любое 
изменение порядка символов. Регистр учитывается, пробелы 
являются существенными.
"""

def is_permutation(a: str, b: str) -> bool:
    A = dict()
    B = dict()
    for symb in a:
        if symb in A:
            A.update({symb: A[symb] + 1})
        else: A.update({symb: 1})

    for symb in b:
        if symb in B:
            B.update({symb: B[symb] + 1})
        else: B.update({symb: 1})

    return A == B



assert is_permutation('baba', 'abab')
assert is_permutation('abbba', 'abab')
