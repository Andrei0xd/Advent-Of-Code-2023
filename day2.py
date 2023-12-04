import re

input = open("./inputs/day2.in", "r")
lines = input.readlines()

game1 = {
    "R": 12,
    "G": 13,
    "B": 14,    
}

ids_sum = 0
min_mult = 0
for line in lines:
    game_id = line.split("Game ")[1].split(":")[0]

    red_pattern = re.compile(" (\d+) red")
    blue_pattern = re.compile(" (\d+) blue")
    green_pattern = re.compile(" (\d+) green")

    reds = red_pattern.findall(line)
    blues = blue_pattern.findall(line)
    greens = green_pattern.findall(line)

    max_red = max([int(x) for x in reds])
    max_blue = max([int(x) for x in blues])
    max_green = max([int(x) for x in greens])
                
    if not (max_red > game1["R"] or max_blue > game1["B"] or max_green > game1["G"]):
        ids_sum += int(game_id)

    min_mult += max_red * max_blue * max_green

print(ids_sum)
print(min_mult)