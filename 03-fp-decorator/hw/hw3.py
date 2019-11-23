from functools import reduce


p6 = sum([i for i in range(1, 101)])**2 - sum([i**2 for i in range(1, 101)])
# print(p6)

p9 = [(a, b, c) for a in range(1001) for b in range(a) for c in range(b) if a**2 + b**2 + c**2 == 1000]
# print(p9)

p40 = reduce(lambda x,y: x*y, [int(list("".join(str(i) for i in range(1, 1000001)))[x-1]) for x in [10**i for i in range(7)]])
# print(p40)

p48 = [i**i for i in range(1, 1001)][-1:-11:-1]
# print(p48)
