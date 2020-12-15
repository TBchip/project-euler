from EulerFunctions import get_all_divisors

abundant_numbers = []
for i in range(1, 28124):
    if sum(get_all_divisors(i, count_x=False)) > i:
        abundant_numbers.append(i)

all_sums = []
for i in range(len(abundant_numbers // 2)):
    for j in range(len(abundant_numbers // 2)):
        sum_ij = abundant_numbers[i] + abundant_numbers[j]
        if sum_ij > 28123:
            break
        all_sums.append(sum_ij)

non_summable = [i for i in range(1, 28123) if i not in all_sums]

print(all_sums)
print(sum(all_sums))
