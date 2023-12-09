from itertools import tee

oasises = []
with open("./inputs/day9.in") as f:
    for line in f:
        oasises.append([int(x) for x in line.strip().split(' ')])

#no python 3.10 :(
def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

#Part 1
def extrapolate_history(oasis):
    if all(x == 0 for x in oasis):
        return 0
    return oasis[-1] + extrapolate_history([y-x for x,y in pairwise(oasis)])

#Part 2
def extrapolate_history2(oasis):
    if all(x == 0 for x in oasis):
        return 0
    return oasis[0] - extrapolate_history2([y-x for x,y in pairwise(oasis)])

print(sum([extrapolate_history(oasis) for oasis in oasises]))
print(sum([extrapolate_history2(oasis) for oasis in oasises]))
