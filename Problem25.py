import EulerFunctions

fibonacci_gen = EulerFunctions.gen_fibonacci_numbers_inf()
i = 1
while True:
    next_num = next(fibonacci_gen)
    if len(str(next_num)) >= 1000:
        print(i)
        break
    i += 1
