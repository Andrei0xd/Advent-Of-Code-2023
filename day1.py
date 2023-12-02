input = open("./inputs/day1.in", "r")
lines = input.readlines()

digits_as_letters = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
}

def check_digit(line, pos):
    if line[pos] > '0' and line[pos] <= '9':
        return int(line[pos])
    l = len(line)
    word = ""
    for j in range (0, len("seven")):
        if pos+j < l:
            word += line[pos+j]
            if word in digits_as_letters:
                return digits_as_letters[word]
        else:
            return 0
    return 0
    
sum = 0
for line in lines:
    p = 0
    c1, c2 = 0,0
    l = len(line)
    while p < l:
        if c1 == 0:
            c1 = check_digit(line, p)
        if c2 == 0:
            c2 = check_digit(line, l-p-1)
        if c1 != 0 and c2 != 0:
            break
        p += 1
        
    sum += c1*10 + c2

print(sum)