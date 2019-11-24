from functools import reduce


def problem9_solver():
    return int(*[a * b * (1000 - b - a) for a in range(1, 1000) for b in range(1, 1000)
                 if a * a + b * b == (1000 - b - a) ** 2 and a < b])


def problem6_solver():
    return sum(i for i in range(101)) ** 2 - sum(i ** 2 for i in range(101))


# Возможно будет разница в единицу,
# т.к. я не учитывал ноль как натуральное число
def problem48_solver():
    return int(str(sum(i ** i for i in range(1, 1001)))[-10:])


def problem40_solver():
    return reduce(lambda x, y: int(x) * int(y),
                  [reduce(lambda x, y: x + y, [str(i) for i in range(185186)])[10 ** i]
                   for i in range(7)])


print(problem9_solver())
print(problem6_solver())
print(problem48_solver())
print(problem40_solver())
