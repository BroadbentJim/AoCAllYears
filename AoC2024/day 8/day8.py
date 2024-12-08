from collections import defaultdict
from math import sqrt
D = open("input.txt").readlines()
D = [x.strip() for x in D]

dict_antenna = defaultdict(set)

for i, l in enumerate(D):
    for j, char in enumerate(l):
        if char != '.':
            dict_antenna[char].add((i,j))

set_antinodes = set()
H,W = len(D), len(D[0])


def is_in_grid(pos):
    return 0<= pos[0] and pos[0] < H and 0 <= pos[1] and pos[1] < W

for freq in dict_antenna:
    antennas = dict_antenna[freq]
    for base in antennas:
        for other in antennas:
            if base == other:
                continue
            displacement = (other[0]-base[0], other[1]-base[1])
            length = sqrt(displacement[0]**2+displacement[1]**2)
            if length % 3 == 0:
                # 4 candidates
                # otherwise 2
                set_antinodes.add((base[0]+displacement[0]*(length/3),base[1]+displacement[1]*(length/3)))
                set_antinodes.add((base[0]+displacement[0]*(2*length/3),base[1]+displacement[1]*(2*length/3)))
            cand = (base[0]-displacement[0],base[1]-displacement[1])
            if is_in_grid(cand):
                set_antinodes.add(cand)
            cand = (other[0]+displacement[0],other[1]+displacement[1])
            if is_in_grid(cand):
                set_antinodes.add(cand)

print(set_antinodes)
for a in set_antinodes:
    assert is_in_grid(a)
    assert isinstance(a[0], int)
print(len(set_antinodes))

# Pt2


set_antinodes = set()
for freq in dict_antenna:
    antennas = dict_antenna[freq]
    for base in antennas:
        for other in antennas:
            if base == other:
                continue
            displacement = (other[0]-base[0], other[1]-base[1])
            length = sqrt(displacement[0]**2+displacement[1]**2)
            test_range = int(H*W // length)
            for scale in range(-test_range, test_range):                
                cand = (base[0]-scale*displacement[0],base[1]-scale*displacement[1])
                if is_in_grid(cand):
                    set_antinodes.add(cand)

print(set_antinodes)
for a in set_antinodes:
    assert is_in_grid(a)
    assert isinstance(a[0], int)
print(len(set_antinodes))