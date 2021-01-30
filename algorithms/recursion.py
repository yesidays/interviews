def recursiveMethod(n):
    if n < 1:
        print('N is less thant 1')
    else:
        recursiveMethod(n-1)
        print(n)


def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwo(n - 1)
        return power * 2


# n! = n * (n-1) * (n-2) * ... * 2 * 1
def factorial(n):
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)


# 1 + 1 + 2 + 3 + 5 + 8 + ...
def fibonacci(n):
    assert n >= 0 and int(n) == n, 'Cannot be negative or non integer'
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Simple recursive method
n = 4
recursiveMethod(n)

power = powerOfTwo(n)
print(f'The power of {n} is {power}\n')


print(f'Factorial of {n} is ')
print(factorial(n))

print(f'Finonacci of {n} is')
print(fibonacci(7))
