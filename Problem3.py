number = 600851475143

prime_list = []
for i in range(10000):
    if i == 0:
        continue

    for j in range(i):
        if (j == 0) or (j == 1):
            continue

        if i % j == 0:
            break
    else:
        prime_list.append(i)

largest_factor = 0
for i in prime_list:
    if number % i == 0:
        largest_factor = i
        number /= i

print(largest_factor)
print(number)
