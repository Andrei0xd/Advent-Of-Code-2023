import re

with open("./inputs/day7.in", "r") as file:
    lines = file.readlines()

xtra = {"J" :0, "T" :10, "Q" :11, "K" :12, "A" :13}

class hand():
    def __init__(self, hashedpairs, bid, hstr):
        self.hashedpairs = hashedpairs
        self.bid = bid
        self.hstr = hstr

    def __lt__(self, other):
        if self.hashedpairs == other.hashedpairs:
            for i in range(len(self.hstr)):
                if not self.hstr[i] == other.hstr[i]:
                    return (int(self.hstr[i]) if self.hstr[i] not in xtra else xtra[self.hstr[i]]) < (int(other.hstr[i]) if other.hstr[i] not in xtra else xtra[other.hstr[i]])
        else:
            return self.hashedpairs < other.hashedpairs

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

    hashedpairs=0
    for s in pairs_hash:
        hashedpairs += 10**s
        
    hands.append(hand(hashedpairs, line.strip().split(" ")[1], handstr))

sum = sum([int(hand.bid)*(r+1) for r,hand in enumerate(sorted(hands))])
print(sum)