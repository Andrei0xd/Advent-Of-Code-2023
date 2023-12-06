import re
import cmath
import math

with open("./inputs/day6.in", "r") as file:
    lines = file.readlines()

times = re.findall('(\d+)',lines[0].split("Time: ")[1].strip())
distances = re.findall('(\d+)',lines[1].split("Distance: ")[1].strip())

def quadratic(a, b, c):
    d = (b**2) - (4*a*c)
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    return abs(sol1), abs(sol2)

def find_min_time(time, distance):
    #Find roots of quadratic equation. we are looking for a, such that (b-a)*a>r, where b is total time and r is distance
    #this means -a^2 + ba - r > 0, find roots of this equation, the difference between the roots is the number of possible values for a
    sol1, sol2 = quadratic(-1, -time, -distance)
    m1 = math.ceil(sol1.real)
    m2 = math.ceil(sol2.real)
    return abs(m1 - m2)

def part_one():
    mult = 1
    for i in range(len(times)):
        time = int(times[i])
        dist = int(distances[i])
        mult *= find_min_time(time, dist)
    return mult
        
def part_two():
    time=0
    dist=0
    for i in range(len(times)):
        time = time*(10**len(times[i])) + int(times[i])
        dist = dist*(10**len(distances[i])) + int(distances[i])
    return find_min_time(time, dist)

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")