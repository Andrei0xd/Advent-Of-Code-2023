import math

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

    subset_count = line.count(";")
    print(subset_count)

    bad_subset = False
    max_red, max_blue, max_green = 0, 0, 0
    for i in range(subset_count+1):
        subset = line.split(";")[i]
        
        if "red" in subset:
            r_count = int(subset.split(" red")[0].split(" ")[-1])
            if r_count > game1["R"]:
                bad_subset = True
            if r_count > max_red:
                max_red = r_count
        
        if "blue" in subset:
            b_count = int(subset.split(" blue")[0].split(" ")[-1])
            if b_count > game1["B"]:
                bad_subset = True
            if b_count > max_blue:
                max_blue = b_count
                
        if "green" in subset:
            g_count = int(subset.split(" green")[0].split(" ")[-1])
            if g_count > game1["G"]:
                bad_subset = True
            if g_count > max_green:
                max_green = g_count
                
    if not bad_subset:
        ids_sum += int(game_id)

    min_mult += max_red * max_blue * max_green

print(ids_sum)
print(min_mult)