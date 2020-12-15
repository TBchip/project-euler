import math

number1_largest = 0
number2_largest = 0
palindrome_largest = 0

for number1 in range(999, 100, -1):
    for number2 in range(999, 100, -1):
        product = number1 * number2
        product_str = str(product)

        half_length = math.floor(len(product_str)/2)
        half1 = product_str[:half_length]
        half2 = product_str[half_length:]

        if half1 == half2[::-1]:
            if product > palindrome_largest:
                number1_largest = number1
                number2_largest = number2
                palindrome_largest = product

print(number1_largest, number2_largest, palindrome_largest)
