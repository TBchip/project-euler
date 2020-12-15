import EulerFunctions


def is_truncatable(x):
    x = str(x)
    for i in range(len(x)):
        if not EulerFunctions.Is_Prime(int(x[i:])):
            return False
    for i in range(len(x)-1):
        if not EulerFunctions.Is_Prime(int(x[:-i-1])):
            return False

    return(True)


prime_gen = EulerFunctions.gen_primes_inf()
while len(str(next(prime_gen))) < 2:
    continue

truncatable_nums = []
while len(truncatable_nums) < 11:
    n = next(prime_gen)
    if is_truncatable(n):
        truncatable_nums.append(n)
        print(n)

print()
print(sum(truncatable_nums))
