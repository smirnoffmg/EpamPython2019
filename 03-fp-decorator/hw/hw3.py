from functools import reduce


# p6 = sum([i for i in range(1, 101)])**2 - sum([i**2 for i in range(1, 101)])
# print(p6)

# p9 = [(a, b, c) for a in range(1001) for b in range(a) for c in range(b) if a**2 + b**2 + c**2 == 1000]
# print(p9)  # довести до ума!

# N = 10*6
# p40 = reduce(lambda x,y: x*y, [int(list("".join(str(i) for i in range(1, N + 1)))[x-1]) for x in [10**i for i in range(7)]])
# print(p40)

# p48 = [i**i for i in range(1, 1001)][-1:-11:-1]
# print(p48)


def return_armstrong_true_or_not(number: int) -> bool:
    """
    Add anotation
    :param number:
    :return:
    """

    result = reduce(lambda sum, it: sum + pow(int(it), len(str(number))),
                    str(number), 0)

    if number == result:
        return "{} is Armstrong number".format(number)
    else:
        return "{} is'nt Armstrong number".format(number)


# print(return_armstrong_true_or_not(153))


count = -1


def return_collatz_count_steps(number: int) -> int:
    """Calculate the number of steps for count

    collatz() that has one parameter named number.
    If number is even, then collatz() should print
    number // 2 and return this value. If number is
    odd, then collatz() should print and return 3 * number + 1.
    """
    global count
    count += 1
    print("count_of_steps", count)
    try:
        number = int(number)
    except ValueError:
        print("Please enter a number correct!")
    else:
        if number == 1:
            return number
        if number % 2 == 0:
            return return_collatz_count_steps(number // 2)
        return return_collatz_count_steps(3 * number + 1)

# print(return_collatz_count_steps("12"))
