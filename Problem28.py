spiral_size = 1001
spiral = [i for i in range(1, spiral_size**2+1)]

diagonal_numbers = [1]

ended = False
r = 1
while not ended:
    for _ in range(4):
        next_diagonal = diagonal_numbers[-1] + r*2

        if next_diagonal > spiral[-1]:
            ended = True
            break

        diagonal_numbers.append(next_diagonal)
    
    r+=1

print(diagonal_numbers)
print(sum(diagonal_numbers))