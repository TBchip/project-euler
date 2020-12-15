import EulerFunctions
import math

import sys

def get_fibonacci_numbers_until(max_num):
    nums = [1, 1]
    while True:
        next_num = nums[-1]+nums[-2]

        if next_num > max_num:
            break

        nums.append(next_num)
    return nums

t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    fibonacci = get_fibonacci_numbers_until(n)