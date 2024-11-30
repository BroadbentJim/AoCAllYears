import os
from collections import Counter

D = open("input.txt").read().splitlines()

two_count = 0
three_count = 0

for line in D:    
    counter = Counter(line)
    if 2 in counter.values():
        two_count += 1
    if 3 in counter.values():
        three_count += 1
print(two_count * three_count)

pair = None
for i, line in enumerate(D[:-1]):    
    for line_pair in D[i+1:]:
        diffs = 0
        for char_0, char_1 in zip(line, line_pair):
            diffs += char_0 != char_1
        if diffs == 1:
            pair = line, line_pair
            break
    if pair:
        break
print(pair)
ans =[]
for char_0, char_1 in zip(pair[0], pair[1]):
    if char_0 == char_1:
        ans.append(char_0)
print("".join(ans))