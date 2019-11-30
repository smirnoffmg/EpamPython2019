from functools import reduce


def return_armstrong_true_or_not(pass_number: int) -> bool:
    """Function determines the Armstrong number in functional form
    and return result - True or False

    Armstrong's number is a natural number, which in a given number
    system is equal to the sum of its digits raised to a power equal
    to the number of its digits.
    """

    result = reduce(lambda x, y: x + pow(int(y), len(str(pass_number))),
                    str(pass_number), 0)
    if pass_number == result:
        return pass_number


number = 153
assert return_armstrong_true_or_not(number) == number, "The number {} is not an Armstrong number".format(number)
