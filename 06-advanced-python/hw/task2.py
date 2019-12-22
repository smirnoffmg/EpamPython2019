"""
Реализовать класс Quaternion, позволяющий работать с кватернионами
https://ru.wikipedia.org/wiki/%D0%9A%D0%B2%D0%B0%D1%82%D0%B5%D1%80%D0%BD%D0%B8%D0%BE%D0%BD
Функциональность (магическими методами):
- сложение
- умножение
- деление
- сравнение
- нахождение модуля
- строковое представление и repr
По желанию:
- взаимодействие с числами других типов
"""
<<<<<<< HEAD


class Quaternion:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __repr__(self):
        return 'Quaternion({}, {}, {}, {})'.format(self.a, self.b, self.c, self.d)

    def __str__(self):
        return '{} + {}i + {}j + {}k'.format(self.a, self.b, self.c, self.d)

    def __add__(self, other):
        return Quaternion(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)

    def __sub__(self, other):
        return Quaternion(self.a - other.a, self.b - other.b, self.c - other.c, self.d - other.d)

    def __mul__(self, other):
        q1_a, q2_a = self.a, other.a
        q1_b, q2_b = self.b, other.b
        q1_c, q2_c = self.c, other.c
        q1_d, q2_d = self.d, other.d
        res_a = q1_a * q2_a - q1_b * q2_b - q1_c * q2_c - q1_d * q2_d
        res_b = q1_a * q2_b + q1_b * q2_a + q1_c * q2_d - q1_d * q2_c
        res_c = q1_a * q2_c - q1_b * q2_d + q1_c * q2_a + q1_d * q2_b
        res_d = q1_a * q2_d + q1_b * q2_c - q1_c * q2_b + q1_d * q2_a

        return Quaternion(res_a, res_b, res_c, res_d)

    def __abs__(self):
        return (self.a ** 2 + self.b ** 2 + self.c ** 2 + self.d ** 2) ** 0.5

    def __truediv__(self, other):
        conj_num = Quaternion(other.a, -other.b, -other.c, -other.d)
        abs_value = abs(conj_num) ** 2
        a, b, c, d = conj_num.a, conj_num.b, conj_num.c, conj_num.d
        inv_num = Quaternion(a/abs_value, b/abs_value, c/abs_value, d/abs_value)
        return self*inv_num

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and\
               self.c == other.c and self.d == other.d


test1 = Quaternion(1, 2, 3, 4)
test2 = Quaternion(4, 3, 2, 1)
test3 = test1 + test2
test4 = test1 - test2
test5 = test1 * test2
test6 = test1 / test2
test7 = test1
test8 = abs(test1)
print(test6)
=======

class Quaternion:
    pass
>>>>>>> upsteam/master
