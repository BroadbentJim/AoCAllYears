from math import lcm

D = open("input8.txt").read()
L = D.splitlines()

ans = 0
pattern = L[0]
pattern = pattern.replace("L", "0")
pattern = pattern.replace("R", "1")
print(pattern)
maps = {}
nodes_starting_with_A = []
for line in L[2:]:
    start, dests = line.split("=")
    start= start[:-1]
    left_dest, right_dest = dests.split(",")
    left_dest = left_dest[2:]
    right_dest = right_dest[1:-1]
    print(start, left_dest, right_dest)
    maps[start] = (left_dest, right_dest)
    if start[-1] == "A":
        nodes_starting_with_A.append(start)
print(nodes_starting_with_A)
print(maps)

time_taken_by_As = []
for start in nodes_starting_with_A:
    print(start)
    i=0
    j=0
    direction = int(pattern[j])
    curr_pos = start
    while curr_pos[-1] != "Z":
        
        directs = maps[curr_pos]
        new = directs[direction]
        print(i,curr_pos, new, directs, direction)
        curr_pos = new
        i += 1
        j = i % len(pattern)
        direction = int(pattern[j])
    print(i)
    time_taken_by_As.append(i)
print(time_taken_by_As)
ans = lcm(*time_taken_by_As)
print(ans)