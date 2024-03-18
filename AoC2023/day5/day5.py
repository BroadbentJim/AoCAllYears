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
    current_chunk.append((source, source+num_range, destination))
groups.append(current_chunk)
# for group in groups: print(group)
# print(len(groups))
min_dist = float('inf')
# for seed in seeds:
#     cur_val = seed
#     for i,map in enumerate(groups):
#         # print(i, cur_val)
#         for shortcut in map:
#             if shortcut[0] <= cur_val and shortcut[1] > cur_val:
#                 # print("Here")
#                 new = cur_val-shortcut[0] + shortcut[2]
#                 cur_val = new
#                 break
#         else:
#             cur_val = cur_val
#     # print(cur_val)
#     min_dist = min(min_dist, cur_val)

#we're composing piecewise linear maps
# So technically this could be done cleverly to build nice mappings
# Need to write some way of writing this composition for two layers

# mega_map = {groups[0]}
# for i, map in enumerate(groups):
#     for shortcut in map:
#         for next_shortcut in groups[i+1]:
#             if shortcut[2] > next_shortcut[0] or shortcut[2]+shortcut[1]-shortcut[0] > next_shortcut[1]:
#                 # if this shortcut maps onto the source of another shortcut
#                 left = max(shortcut[2], next_shortcut[0])
#                 right = min(shortcut[2]+shortcut[1]-shortcut[0],next_shortcut[1])
#                 image = destination + left -next_shortcut[0]
    
for j, seed_pair in enumerate(seed_pairs):
    print("="*80)
    print(j)
    print("="*80)
    for i in range(seed_pair[0], seed_pair[0]+seed_pair[1]):
        cur_val = i
        for i,map in enumerate(groups):
            # print(i, cur_val)
            for shortcut in map:
                if shortcut[0] <= cur_val and shortcut[1] > cur_val:
                    # print("Here")
                    new = cur_val-shortcut[0] + shortcut[2]
                    cur_val = new
                    break
            else:
                cur_val = cur_val
        # print(cur_val)
        min_dist = min(min_dist, cur_val)

print(min_dist)
            