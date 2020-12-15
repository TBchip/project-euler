import math


def is_factorial_of_digits(x):
    x_list = list(str(x))

    sum_factorial_digits = 0
    for i in x_list:
        sum_factorial_digits += math.factorial(int(i))

    if sum_factorial_digits == x:
        return True
    return False


sum_digits_factorial = []
for i in range(3, 10000000):
    if is_factorial_of_digits(i):
        sum_digits_factorial.append(i)

    # debuging
    if i % 100000 == 0:
        print(i)

print()
print(sum_digits_factorial)
print(sum(sum_digits_factorial))
