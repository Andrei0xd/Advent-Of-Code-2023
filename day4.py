import re
import math

input = open("./inputs/day4.in", "r")
lines = input.readlines()

part1_sum = 0
num_of_cards = len(lines)

winning_amounts = [1] * (num_of_cards)

for i in range(num_of_cards):
    line = lines[i]
    cards_pattern = re.compile(r"Card\s*(\d+): ")
    cards = cards_pattern.split(line)[0::2][1].strip()
    card_num = int(cards_pattern.match(line).group(1))

    card_num_pattern = re.compile("\d+")
    winning_cards = set([int(s) for s in card_num_pattern.findall(cards.split(" | ")[0])])
    my_cards = set([int(s) for s in card_num_pattern.findall(cards.split(" | ")[1])])

    num_of_winning_cards = len(winning_cards.intersection(my_cards))

    if num_of_winning_cards > 0:
        part1_sum += math.pow(2, num_of_winning_cards - 1)

    print(winning_amounts)
    for i in range(num_of_winning_cards):
        if i+card_num>=num_of_cards:
            break
        winning_amounts[card_num+i] += winning_amounts[card_num-1]

part2_sum = sum(winning_amounts)

print(part1_sum)
print(part2_sum)


