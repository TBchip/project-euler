numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

output = 0
while True:
    output += 10
    if output % 1000000 == 0:
        print(output)

    for i in numbers:
        if output % i != 0:
            break
    else:
        print()
        print(output)
        break
