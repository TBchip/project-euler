import numpy as np

fibonacci = [1, 2]

next_number = fibonacci[-1] + fibonacci[-2]
while next_number <= 4000000:
    fibonacci.append(next_number)
    next_number = fibonacci[-1] + fibonacci[-2]

print(fibonacci)

sum_fibonacci = 0
for number in fibonacci:
    if number % 2 == 0:
        sum_fibonacci += number

print(sum_fibonacci)
