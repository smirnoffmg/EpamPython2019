
"""Problem 6"""
from functools import reduce

n = 100
p6 = sum([i for i in range(1, n + 1)]) ** 2 - sum([i ** 2 for i in range(1, n + 1)])
print(p6)


""" Problem 9. Introduction
Because of the ratio of a, b, c in a Pythagorean triplet no variable can ever be
larger than half the sum of a + b + c therefore I have lowered the upper limit to 500 or sum_elements // 2 """

sum_elements = 1000
half_sum = sum_elements // 2
p9 = [(a, b, 1000 - (a + b)) for a in range(1, half_sum) for b in range(a + 1, half_sum) if
      a ** 2 + b ** 2 == (sum_elements - (a + b)) ** 2]
print("a = {0}, b = {1}, c = {2}".format(*p9[0]))


"""Problem 40"""
N = 10**6
p40 = reduce(lambda x, y: x*y, [int(list("".join(str(i) for i in range(1, N + 1)))[x-1])
                               for x in [10**i for i in range(7)]])

print("The value of the following expression is {}".format(p40))


"""Problem 48"""
p48 = [i ** i for i in range(1, 1001)][-1:-11:-1]
print("Last {len_last_list_elements} elements is {value}\n".format(len_last_list_elements=len(p48),
                                                             value=p48))
