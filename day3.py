import math

input = open("./inputs/day3.in", "r")
lines = input.readlines()

SYMBOLS = ["#", "@", "!", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "~", "`", "[", "]", "{", "}", "|", "\\", "/", "?", ">", "<", ",", ":", ";", "'", "\""]

gears = {}

#Append dots at the top and bottom for easier parsing/no bound checking
append_dot = "."*len(lines[0])
lines = [append_dot] + lines + [append_dot]

#On each line, append a dot at the beginning and end for easier parsing/no bound checking
for i in range(len(lines)):
    lines[i] = "." + lines[i] + "."

#It passed AoC's test, but issue arrises when there are multiple * symbols neighbouring the same number
def check_position(i, j, lines, gear):
    if lines[i][j] in SYMBOLS:
        if lines[i][j] == "*":
            gear[0] = i
            gear[1] = j
        return True

def check_neighbours(i, j, lines, gear):
    return check_position(i-1, j, lines, gear) or \
        check_position(i+1, j, lines, gear) or \
        check_position(i, j-1, lines, gear) or \
        check_position(i, j+1, lines, gear) or \
        check_position(i-1, j-1, lines, gear) or \
        check_position(i-1, j+1, lines, gear) or \
        check_position(i+1, j-1, lines, gear) or \
        check_position(i+1, j+1, lines, gear)

sum=0
for i in range(len(lines)):
    line = lines[i]
    j=0
    while j < len(line):
        if line[j] >= '0' and line[j] <= '9':
            x = j
            has_neighbour = False
            gear=[0,0]
            while line[x] >= '0' and line[x] <= '9':
                has_neighbour = check_neighbours(i, x, lines, gear) or has_neighbour
                x+=1
            if has_neighbour:
                sum+=int(line[j:x])
                
            if gear[0] != 0 and gear[1] != 0:
                g=(gear[0], gear[1])
                if g in gears:
                    gears[g].append(int(line[j:x]))
                else:
                    gears[g] = [int(line[j:x])]
            j = x
        j+=1

print(f"Part 1: {sum}")

gear_sum=0
for gear in gears:
    if len(gears[gear]) == 2:
        gear_sum+=math.prod(gears[gear])
print(f"Part 2: {gear_sum}")