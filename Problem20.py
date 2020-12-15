import math

factorial = math.factorial(100)
factorial_str = str(factorial)
factorial_list = [int(i) for i in factorial_str]
factorial_sum = sum(factorial_list)
print(factorial_sum)
