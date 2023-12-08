import math
from functools import reduce

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

with open("./inputs/day8.in", "r") as file:
    lines = file.readlines()
        
instructions = lines[0].strip()

nodes = {}
for line in lines[2:]:
    nodes[line.split(" ")[0]] = (
        line.split(" ")[2].split("(")[1].split(",")[0],
        line.split(" ")[3].split(")")[0],
    )


####################### PART 1 #######################
def walk(start, end_node_ending):
    current_node = start
    instruct_index = 0
    while str(current_node[:len(end_node_ending)]) != end_node_ending:
        walk_dir = 1 if instructions[instruct_index%len(instructions)] == "R" else 0
        current_node = nodes[current_node][walk_dir]
        instruct_index += 1
    return instruct_index
print(walk("AAA", "ZZZ"))




####################### PART 2 #######################
start_nodes = [node for node in nodes if node[-1] == "A"]
end_nodes = [node for node in nodes if node[-1] == "Z"]

#It works for current input, but it is not a general solution.
def check_done():
    for start_node in start_nodes:
            if not end_distances.get(start_node):
                return False
    return True

end_distances = {}
i = 0
walking_nodes = start_nodes.copy()
while not check_done():
    walk_dir = 1 if instructions[i%len(instructions)] == "R" else 0
    next_nodes = []
    for index, walking_node in enumerate(walking_nodes):
        next_node = nodes[walking_node][walk_dir]
        if next_node in end_nodes:
            started_from = start_nodes[index]
            if not end_distances.get(started_from):
                end_distances[started_from] = {}
            if not end_distances[started_from].get(next_node):
                end_distances[started_from][next_node] = i+1
        next_nodes.append(next_node)
    walking_nodes = next_nodes
    i += 1

ends = [end_distances[start_node][end_node] for start_node in start_nodes for end_node in end_nodes if end_distances[start_node].get(end_node)]
print(reduce(lambda x, y: lcm(x, y), ends))