def sum_of_powers(x, power):
    x_str = str(x)
    power_sum = sum([int(i) ** power for i in x_str])
    return x == power_sum


output = []

for i in range(10, 1000000):
    if sum_of_powers(i, 5):
        output.append(i)


print(output)
print(sum(output))
