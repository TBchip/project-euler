from EulerFunctions import Get_Primes_range

primes = Get_Primes_range(0, 100000)

def consecutive_primes(a, b):
    n = 0
    while n**2 + a*n + b in primes:
        n+=1
    
    return n


ab_values = Get_Primes_range(0, 1001)

#format: consecutive_primes, a, b
highest_consecutive_primes = [0, 0, 0]
for a in range(-1000, 1000):
    for b in ab_values:
        amount = consecutive_primes(a,b)
        if amount > highest_consecutive_primes[0]:
            highest_consecutive_primes[0] = amount
            highest_consecutive_primes[1] = a
            highest_consecutive_primes[2] = b
    print(a)

print(highest_consecutive_primes)
print(highest_consecutive_primes[1] * highest_consecutive_primes[2])