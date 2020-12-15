def alphabet_index_sum(x):
    indexes = []
    for i in x:
        indexes.append(alphabet[1][alphabet[0].index(i)])

    return sum(indexes)


alphabet = [[i for i in "abcdefghijklmnopqrstuvwxyz"],
            [i for i in range(1, 27)]]

names = []
with open("ProblemFiles/Problem22Names.txt", "r") as names_file:
    names_str = names_file.read()
    names = names_str.split("\",\"")

names = sorted(names)
namescore_sum = 0

for name in names:
    namescore = alphabet_index_sum(name.lower()) * (names.index(name)+1)
    namescore_sum += namescore

print(namescore_sum)
