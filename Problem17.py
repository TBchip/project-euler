from num2words import num2words


def count_letters(x):
    x = str.replace(x, " ", "")
    x = str.replace(x, "-", "")
    return len(x)


letters = 0
for i in range(1, 1001):
    letters += count_letters(num2words(i))
    print(letters)

print(letters)
