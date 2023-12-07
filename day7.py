import re

with open("./inputs/day7.in", "r") as file:
    lines = file.readlines()

overten = ["T","Q", "K", "A"]

class hand():
    def __init__(self, hashedpairs, bid, handstr):
        self.hashedpairs = hashedpairs
        self.bid = bid
        self.handstr = handstr

    def __lt__(self, other):
        if self.hashedpairs < other.hashedpairs:
            return True
        elif self.hashedpairs == other.hashedpairs:
            for i in range(len(self.handstr)):
                a = 0 if self.handstr[i] == "J" else (int(self.handstr[i]) if self.handstr[i] not in overten else 10+overten.index(self.handstr[i]))
                b = 0 if other.handstr[i] == "J" else (int(other.handstr[i]) if other.handstr[i] not in overten else 10+overten.index(other.handstr[i]))
                if a < b:
                    return True
                elif a > b:
                    return False
        else:
            return False

hands = []
for line in lines:
    bid = line.strip().split(" ")[1]
    handstr = line.strip().split(" ")[0]

    handstrsort = ''.join(sorted(handstr))
    pairs = re.finditer(r"(.)\1*", handstrsort)
    
    pairs_hash = []
    jokers = handstrsort.count("J")
    
    if handstrsort.count("J") == 5:
        jokers = 0
        pairs_hash.append(5)

    for i, pair in enumerate(pairs):
        if pair.group(0)[0] == "J":
            continue
        pairs_hash.append(len(pair.group(0)))

    pairs_hash[pairs_hash.index(max(pairs_hash))] = max(pairs_hash)+jokers

    hashedpairs=0
    for s in pairs_hash:
        hashedpairs += (10**(s-1))*s
        
    hands.append(hand(hashedpairs, bid, handstr))

sum = sum([int(hand.bid)*(r+1) for r,hand in enumerate(sorted(hands))])
print(sum)