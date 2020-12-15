for c in range(1000):
    if c < 333:
        continue

    c_squared = c**2

    for b in range(c):
        b_squared = b**2

        for a in range(b):
            a_squared = a**2

            if a_squared + b_squared != c_squared:
                continue

            if a + b + c == 1000:
                print("found")
                print(a)
                print(b)
                print(c)
                print(f"product: {a * b * c}")
