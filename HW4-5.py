from functools import reduce


def func(num1, num2):
    return num1 * num2


print(reduce(func, [num for num in range(100, 1001) if num % 2 == 0]))
