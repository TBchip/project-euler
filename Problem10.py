import EulerFunctions

primes = EulerFunctions.Get_Primes_range(0, 2000000)
sum_primes = sum(primes)

print(sum_primes)
