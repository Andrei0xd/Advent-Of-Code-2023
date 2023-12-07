import re, functools

with open("./inputs/day7.in", "r") as file:
    lines = file.readlines()

xtra = {"J" :0, "T" :10, "Q" :11, "K" :12, "A" :13}

def comparator(self, other):
    if self[0] == other[0]:
        for i in range(len(self[1])):
            if not self[1][i] == other[1][i]:
                return (int(self[1][i]) if self[1][i] not in xtra else xtra[self[1][i]]) - (int(other[1][i]) if other[1][i] not in xtra else xtra[other[1][i]])
    else:
        return self[0] - other[0]
        
hands = []
for line in lines:
    handstr = line.strip().split(" ")[0]
    handstrsort = ''.join(sorted(handstr))
    pairs = re.finditer(r"(.)\1*", handstrsort)
    
    pairs_hash = []
    jokers = handstrsort.count("J")%5

    for i, pair in enumerate(pairs):
        if not (pair.group(0)[0] == "J" and len(pair.group(0)) < 5):
            pairs_hash.append(len(pair.group(0)))

    pairs_hash[pairs_hash.index(max(pairs_hash))] = max(pairs_hash)+jokers

    hashedpairs=sum([10**s for s in pairs_hash])
    
    hands.append((hashedpairs,  handstr, line.strip().split(" ")[1]))

sum = sum([int(hand[2])*(r+1) for r,hand in enumerate(sorted(hands, key=functools.cmp_to_key(comparator)))])
print(sum)