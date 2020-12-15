import math
import EulerFunctions
from itertools import permutations


def Gen_Family(family_type):
    family = []
    for i in range(10):
        family.append(family_type.replace("-", str(i)))

    return family


family_length = 8
length = 6

print("generating combinations")
combinations = [i for i in permutations(
    "0-" * length, length) if ("-" in i) and ("0" in i)]
combinations = [list(i) for i in dict.fromkeys(combinations)]

print()
print("generating primes")
primes = EulerFunctions.Gen_Primes_range(int("1" + "0"*(length-1)), int("9"*length))

print()
print("generating prime family types")
prime_family_types = []
for prime in primes:

    prime = str(prime)
    for combination in combinations:

        temp_prime = list(prime)
        for i in range(length):
            if combination[i] == "-":
                temp_prime[i] = "-"

        prime_family_types.append("".join(temp_prime))

prime_family_types = [i for i in dict.fromkeys(prime_family_types)]

print()
print("generating prime families")
prime_families = []
for prime_family_type in prime_family_types:
    family = Gen_Family(prime_family_type)
    prime_family = [i for i in family if EulerFunctions.Is_Prime(int(i))]
    prime_families.append(prime_family)

print()
print(f"looking for length {family_length} prime families")
prime_families_length_8 = [i for i in prime_families if len(i) == 8]

print()
print("found:")
print(prime_families_length_8)
