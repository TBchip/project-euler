import itertools

permutations = [list(i) for i in itertools.permutations("0123456789")]
print("".join(permutations[999999]))
