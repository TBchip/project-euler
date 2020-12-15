highest_triangle_number_divisions = [0, 0]
triangle_number = 0
i = 1
while highest_triangle_number_divisions[1] < 500:
    divisions = 3

    triangle_number += i
    if triangle_number % 2 == 0:

        for j in range(3, triangle_number):
            if triangle_number % j == 0:
                divisions += 1

        if divisions > highest_triangle_number_divisions[1]:
            highest_triangle_number_divisions = [triangle_number, divisions]
            print()
            print()
            print("------------")
            print(highest_triangle_number_divisions[0])
            print(highest_triangle_number_divisions[1])
            print("------------")
            print()
        else:
            print()
            print(triangle_number)
            print(divisions)

    i += 1

print()
print()
print("---------------------------------------")
print(highest_triangle_number_divisions[0])
print(highest_triangle_number_divisions[1])
