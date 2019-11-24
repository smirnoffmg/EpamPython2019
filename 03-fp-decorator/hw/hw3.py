
def collatz_steps(n):
    counter = 0
    if n == 1:
        return counter
    counter += 1
    if n % 2 == 0:
        counter += collatz_steps(n/2)
    else:
        counter += collatz_steps(3*n+1)
    return counter


assert collatz_steps(16) == 4
assert collatz_steps(12) == 9
assert collatz_steps(1000000) == 152