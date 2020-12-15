def is_nontrivial(x, y):
    x_str = str(x)
    y_str = str(y)

    z1 = x/y
    z2 = int(x_str[0]) / int(y_str[-1])

    if z1 == z2:
        return True

    return False


fractions = []
for i in [a for a in range(10, 100) if (str(a)[-1] != str(a)[-2]) and ("0" not in str(a))]:
    for j in [b for b in range(10, 100) if (str(i)[-1] == str(b)[-2]) and ("0" not in str(b)) and (b > i)]:
        if is_nontrivial(i, j):
            print(i, j)
