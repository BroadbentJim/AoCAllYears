D = open("input1.txt").read().splitlines()

left = []
right = []

for line in D:
    l,r = line.split("   ")
    left.append(int(l))
    right.append(int(r))

left = sorted(left)
right = sorted(right)

ans = 0
for l,r in zip(left,right):
    ans += abs(l-r)
print(ans)

from collections import Counter

counter = Counter(right)

ans = 0
for num in left:
    ans += num * counter[num]
print(ans)