from functools import reduce

"""Problem 6. Sum square difference"""

n = 100

p6 = sum([i for i in range(1, n + 1)]) ** 2 - sum([i ** 2 for i in range(1, n + 1)])

print(p6)

""" Problem 9. Special Pythagorean triplet. Introduction
Because of the ratio of a, b, c in a Pythagorean triplet no variable can ever be
larger than half the sum of a + b + c therefore I have lowered the upper limit to 500 or sum_elements // 2 """

sum_elements = 1000
half_sum = sum_elements // 2

p9 = [(x, y, 1000 - (x + y)) for x in range(1, half_sum) for y in range(x + 1, half_sum) if
      x ** 2 + y ** 2 == (sum_elements - (x + y)) ** 2]

print("x = {0}, y = {1}, c = {2}".format(*p9[0]))

"""Problem 40. Champernowne's constant
An irrational decimal fraction is created by concatenating the positive integers:

                        0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part, 
find the value of the following expression.

                d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000"""

N = 10**6

p40 = reduce(lambda x, y: x*y, [int(list("".join(str(i) for i in range(1, N + 1)))[x-1])
                                for x in [10**i for i in range(7)]])

print("The value of the following expression is {}".format(p40))


"""Problem 48. Find the last ten digits of the series"""
stop = 1000
start = stop - 9
p48 = sum([i ** i for i in range(start, stop + 1)])
print(p48)