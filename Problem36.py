import math


def is_palindrome(x):
    for i in range(math.ceil(len(x)/2)):
        if x[i] != x[-i-1]:
            return False

    return True


double_palindromes = []
for i in range(1000000):
    if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
        double_palindromes.append(i)
        print(i)

print()
print(sum(double_palindromes))
