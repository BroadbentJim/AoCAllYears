from collections import defaultdict

D = open("input.txt").read().splitlines()

ans = 0
used = defaultdict(int)

for line in D:
    items = line.split()
    offset, hw, = items[2], items[3]
    dist_left,dist_top = offset.split(",")
    dist_left = int(dist_left)
    dist_top = int(dist_top.strip(":"))

    h,w = (int(x) for x in hw.split("x"))
    print(line)
    print(dist_left,dist_top,h,w)
    for x in range(dist_left, dist_left+w):
        for y in range(dist_top, dist_top+h):
            used[(x,y)] += 1
            # if len(used) > 1:
            #     ans += 1
for key,x in used.items():    
    if (x > 1):
        print(x)
        ans += 1
print(ans)