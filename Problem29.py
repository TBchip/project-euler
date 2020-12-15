from itertools import product

ab_range = [i for i in range(2, 101)]

combs = [list(i) for i in product(ab_range, ab_range)]

powers = []
for i in combs:
    powers.append(i[0] ** i[1])

powers = list(dict.fromkeys(powers))

print(powers)
print(len(powers))