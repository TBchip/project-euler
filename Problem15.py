import math

grid_size = 20

routes_count = math.factorial(
    grid_size*2) / math.factorial(grid_size) / math.factorial(grid_size)

print(routes_count)
