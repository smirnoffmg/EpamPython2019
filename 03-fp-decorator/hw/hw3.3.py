def return_collatz_count_steps(pass_number: int, count=0) -> int:
    """Calculate count of number steps to satisfy the condition:
    number == 1

    collatz() that has one parameter named number.
    If number is even, then collatz() should print
    number // 2 and return this value. If number is
    odd, then collatz() should print and return 3 * number + 1.
    """
    try:
        pass_number = int(pass_number)
    except ValueError:
        print("Please enter a number correct!")
    else:
        if pass_number == 1:
            return count
        elif pass_number % 2 == 0:
            count += 1
            return return_collatz_count_steps(pass_number // 2, count=count)
        else:
            count += 1
            return return_collatz_count_steps(3 * pass_number + 1, count=count)


assert int(return_collatz_count_steps(2)) == 1
assert return_collatz_count_steps(12) == 9
assert return_collatz_count_steps(1000000) == 152
