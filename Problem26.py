
def scale_divide(x):
    return scale_factor//x


def get_repitition(x):
    result = scale_divide(x)
    result = str(result)

    padding = "0" * ((len_scale_factor-1) - len(result))
    result = padding + result

    repitition = recurring_cycle(result)
    result = result[0:repitition[1]]

    print("0." + result + f"({repitition[0]})")
    return repitition


def recurring_cycle(x):
    l = len(x)
    start = 0
    end = 1
    for _ in range(l-1):
        for _ in range(l):
            p0 = x[start:start+end]
            p1 = x[start+end:start+end*2]
            p2 = x[start+end*2:start+end*3]
            if p0 == p1 and p0 == p2:
                return [p0, start]

            end += 1
        start += 1
        end = 1


len_scale_factor = 10000
scale_factor = int("1" + "0" * (len_scale_factor-1))

len_highest_rep = 0
highest_rep = 0
highest_rep_division = 0
for i in range(2, 1000):
    print()
    print(f"---{i}---")
    rep = get_repitition(i)
    len_rep = len(rep[0])
    if len_rep > len_highest_rep:
        len_highest_rep = len_rep
        highest_rep = rep[0]
        highest_rep_division = i

print()
print("-------------------")
print()
print("repitition:")
print(highest_rep)
print()
print("length repitition:")
print(len_highest_rep)
print()
print("division:")
print(highest_rep_division)
print()
print("length scalefactor:")
print(len_scale_factor)
