from functools import reduce


def is_armstrong(number):
    return reduce(lambda x,y: x+y, map(lambda x: int(x)**len(str(number)),
                                   str(number))) == number


assert is_armstrong(153) == True, 'Число Армстронга'
assert is_armstrong(10) == False, 'Не число Армстронга'