primes = [2, 3, 5, 7, 11]

i = 11
while len(primes) < 10001:
    i += 1
    for prime in primes:
        if i % prime == 0:
            break
    else:
        primes.append(i)

print(primes[-1])
