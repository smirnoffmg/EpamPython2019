"""
В начале файла содержится текст задания
"""


def test_some_function(*args, **kwargs):
    """
	Некоторые дополнительные пояснения, если они нужны и касаются именно тела функции
	"""
    return 0


# Тесты для проверки
assert test_some_function() == 0
assert test_some_function() == -1
