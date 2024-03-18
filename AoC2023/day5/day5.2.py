from bisect import insort, bisect_right


def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError


def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

D = open("input5.txt")
seed_line = next(D)
seeds = seed_line.split(":")[1]
seeds = [int(x) for x in seeds.split()]
print(seeds)
seed_pairs = [(seeds[i], seeds[i+1]) for i in range(0,len(seeds),2)]
print(seed_pairs)
next(D)
groups = []
current_chunk = []
for line in D:
    # print(line, current_chunk)
    if not line.strip():
        groups.append(current_chunk)
        current_chunk = []
        continue
    if not line[0].isdigit():
        # terms = line.split("-")
        # input, output = terms[0], terms[2]
        continue
    nums = [int(x) for x in line.split()]
    destination, source, num_range = nums
    # for i in range(num_range):
    #     current_chunk[source+i] = destination +i
    # current_chunk.append((source, source+num_range, destination))
    insort(current_chunk, (destination, num_range, source))
groups.append(current_chunk)
# for group in groups: print(group)
# print(len(groups))
min_dist = float('inf')

#we're composing piecewise linear maps
# So technically this could be done cleverly to build nice mappings
# Need to write some way of writing this composition for two layers

# mega_map = groups[0]
# for map in enumerate(groups[1:]):
#     new_mega_map = []
#     for shortcut in mega_map:
#         next_shortcut = find_le(map, shortcut[2])
#         if next_shortcut[1] > shortcut[2]:
#             #Intersect
#             left = max(next_shortcut[0], shortcut[0])
#             right = min(next_shortcut[1], shortcut[2]+shortcut[1]-shortcut[0])
            
i = 0
going = True
while going:
    if i % 10e5 == 0:
        print(i)
    prev_value = i
    for amap in groups[::-1]:
        try:
            shortcut = find_le(amap, (prev_value,prev_value,prev_value))
            if shortcut[0]+shortcut[1] > prev_value:
                prev_value = shortcut[2]+prev_value-shortcut[0]
        except:
            prev_value = prev_value
        # for shortcut in amap:
        #     if shortcut[2] <= prev_value and  prev_value < shortcut[2]+shortcut[1]:
        #         prev_value = shortcut[0] + prev_value - shortcut[2]
        #         break
    for seed_pair in seed_pairs:
        if seed_pair[0] < prev_value and prev_value < seed_pair[0]+seed_pair[1]:
            ans = i
            going = False
            break
    i += 1
print("ANS")            
print(ans)
            