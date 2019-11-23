from functools import reduce


# p6 = sum([i for i in range(1, 101)])**2 - sum([i**2 for i in range(1, 101)])
# print(p6)

# p9 = [(a, b, c) for a in range(1001) for b in range(a) for c in range(b) if a**2 + b**2 + c**2 == 1000]
# print(p9)

# p40 = reduce(lambda x,y: x*y, [int(list("".join(str(i) for i in range(1, 1000001)))[x-1]) for x in [10**i for i in range(7)]])
# print(p40)

# p48 = [i**i for i in range(1, 1001)][-1:-11:-1]
# print(p48)


def return_armstrong_true_or_not(number: int) -> bool:

    result = reduce(lambda sum, it: sum + pow(int(it), len(str(number))),
                     str(number), 0)

    if number == result:
        return "{} is Armstrong number".format(number)
    else:
        return "{} is'nt Armstrong number".format(number)

# print(return_armstrong_true_or_not(153))

def collatz_steps(number: int) -> int:
    while number > 1:
        count_steps = (number // 2) if number % 2 == 0 \
            else (number * 3 + 1)
        return count_steps

# print(collatz_steps(11))