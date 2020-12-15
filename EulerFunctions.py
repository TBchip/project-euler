import math


def Is_Prime(x):
    if x == 2:
        return True

    if (x % 2 == 0) or (x == 1):
        return False

    max_division = math.ceil(math.sqrt(x))
    for i in range(3, max_division+1, 2):
        if x % i == 0:
            return False

    return True


def Get_Primes_range(minimum, maximum):
    return [i for i in range(minimum, maximum) if Is_Prime(i)]


def Get_Primes_amount(amount):
    primes = []
    i = 1
    while len(primes) < amount:
        if Is_Prime(i):
            primes.append(i)
        i += 1

    return primes


def gen_primes_inf():
    i = 1
    while True:
        if Is_Prime(i):
            yield i
        i += 1


def get_all_divisors(x, count_one=True, count_x=True):
    divisors = []

    if count_one:
        divisors.append(1)
    if count_x:
        divisors.append(x)

    max_divisor = math.ceil(math.sqrt(x))

    for i in range(2, max_divisor):
        if x % i == 0:
            divisors.append(i)
            divisors.append(int(x/i))

    return sorted(divisors)


def get_fibonacci_numbers_amount(amount):
    nums = [1, 1]
    for _ in range(amount-2):
        nums.append(nums[-1]+nums[-2])
    return nums


def get_fibonacci_numbers_until(max_num):
    nums = [1, 1]
    while True:
        next_num = nums[-1]+nums[-2]

        if next_num > max_num:
            break

        nums.append(next_num)
    return nums


def gen_fibonacci_numbers_inf():
    nums = [1, 1]
    yield nums[0]
    yield nums[1]
    while True:
        nums.append(nums[-1]+nums[-2])
        yield nums[-1]
