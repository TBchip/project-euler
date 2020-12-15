import math


def is_pandigital(x, y):
    z = x*y

    number_str = "".join(sorted(str(x) + str(y) + str(z)))
    numbers = "123456789"

    if number_str == numbers:
        return True

    return False


pandigital_products = []

for num1 in range(2, 5000):
    for num2 in [i for i in range(2, 5000) if len(str(num1*i) + str(num1) + str(i)) == 9]:
        if is_pandigital(num1, num2):
            pandigital_products.append(num1*num2)
    print(f"{num1}/4999")

pandigital_products = list(dict.fromkeys(pandigital_products))
pandigital_products = sorted(pandigital_products)

print()
print("-------------------------------------------")
print()
print("pandigital products:")
print(pandigital_products)
print("length:")
print(len(pandigital_products))
print()
print("sum:")
print(sum(pandigital_products))
