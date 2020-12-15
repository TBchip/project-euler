import math


def get_all_divisors(x):
    divisors = []

    for i in range(1, x):
        if x % i == 0:
            divisors.append(i)

    return divisors


checked_numbers = []
amicable_numbers = []


for i in range(1, 10000):
    if i in checked_numbers:
        continue

    sum_divisors = sum(get_all_divisors(i))
    num2_sumdivisors = sum(get_all_divisors(sum_divisors))

    if num2_sumdivisors == i:
        amicable_numbers.append(i)
        if sum_divisors < 10000:
            amicable_numbers.append(sum_divisors)

    checked_numbers.append(i)
    checked_numbers.append(sum_divisors)

amicable_numbers = [
    i for i in amicable_numbers if amicable_numbers.count(i) == 1]

print(amicable_numbers)
print(sum(amicable_numbers))
print(len(amicable_numbers))
