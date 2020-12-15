from EulerFunctions import Get_Primes_range
from EulerFunctions import Is_Prime
from itertools import permutations


def is_circular_prime(x):
    x = list(str(x))

    for _ in range(len(x)):
        x.append(x[0])
        x.pop(0)
        if not Is_Prime(int("".join(x))):
            return False

    return True


primes_to_milion = Get_Primes_range(2, 1000001)

circular_primes = []
for i in primes_to_milion:
    if is_circular_prime(i):
        circular_primes.append(i)

    print(i)

print(circular_primes)
print(len(circular_primes))
