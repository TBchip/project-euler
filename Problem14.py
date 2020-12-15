def get_chain_length(n, chainlength=0):

    chainlength += 1
    if n == 1:
        return chainlength

    if n % 2 == 0:
        chainlength = get_chain_length(n/2, chainlength)
    else:
        chainlength = get_chain_length(3*n+1, chainlength)

    return chainlength


largest_chainlength_number = 0
largest_chainlength = 0

for i in range(1, 1000000):
    if i % 2 == 0:
        continue

    print(i)
    chainlength = get_chain_length(i)

    if chainlength > largest_chainlength:
        largest_chainlength = chainlength
        largest_chainlength_number = i

print(largest_chainlength_number)
print(largest_chainlength)
