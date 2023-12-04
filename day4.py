import re
import math

with open("./inputs/day4.in", "r") as file:
    lines = file.readlines()

part1_sum = 0
num_of_cards = len(lines)
winning_amounts = [1] * num_of_cards

for i, line in enumerate(lines):
    card_num = int(re.search(r"Card\s*(\d+):", line).group(1))
    cards = line.split(":")[1].strip()
    winning_cards = set(map(int, re.findall(r"\d+", cards.split(" | ")[0])))
    my_cards = set(map(int, re.findall(r"\d+", cards.split(" | ")[1])))

    num_of_winning_cards = len(winning_cards & my_cards)
    part1_sum += 2 ** (num_of_winning_cards - 1) if num_of_winning_cards > 0 else 0

    for j in range(num_of_winning_cards):
        if card_num + j < num_of_cards:
            winning_amounts[card_num + j] += winning_amounts[card_num - 1]
        else:
            break

part2_sum = sum(winning_amounts)

print(part1_sum)
print(part2_sum)
