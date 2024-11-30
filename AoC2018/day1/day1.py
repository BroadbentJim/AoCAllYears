import os

D = open("input.txt").readlines()
ans = 0
# print(D)
visited = {0}
i = 0
while True:
    line = D[i % len(D)]
    line = line.strip()
    char = line[0]
    if char == '+':
        ans += int(line[1:])
    else:
        ans -= int(line[1:])
    if ans in visited:
        print(ans, ans)
        break
    visited.add(ans)
    i += 1
# print(visited)
# print(ans)