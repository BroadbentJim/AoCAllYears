D = open("input11.txt").read().splitlines()

W = len(D[0])
H = len(D)
MILLION = int(1e6)
# MILLION = 100
# print(MILLION)
missing_cols = list(range(W))
missing_rows = list(range(H))

# print(missing_cols)
galaxy_locations = []
for i, line in enumerate(D):
    for j, char in enumerate(line):
        if char == "#":
            if j in missing_cols:
                missing_cols.remove(j)
            if i in missing_rows:
                missing_rows.remove(i)
            galaxy_locations.append([i,j])

# print(galaxy_locations)
for col in reversed(missing_cols):
    for i, loc in enumerate(galaxy_locations):
        if loc[1] > col:
            new_loc = [loc[0], loc[1]+ MILLION-1]
            galaxy_locations[i] = new_loc
for row in reversed(missing_rows):
    for i, loc in enumerate(galaxy_locations):
        if loc[0] > row:
            new_loc = [loc[0]+MILLION-1, loc[1]]
            galaxy_locations[i] = new_loc
print(galaxy_locations)
#Then insert the bonus rows, cols
#Go backwards over missing rows, and cols
# And move things
# print(missing_cols)
# print(missing_rows)

# for col in reversed(missing_cols):
#     D = [x[:col] + ("." * int(1e6)) + x[col:] for x in D]
# W = len(D[0])
# for row in reversed(missing_rows):
#     D = D[:row] + [("." * W * int(1e6))] + D[row:]
# H = len(D)
# assert all([len(x) == W for x in D])
# print(D)
# galaxy_locations = []
# for i, line in enumerate(D):
#     for j, char in enumerate(line):
#         if char == "#":
#             galaxy_locations.append([i,j])

# print(galaxy_locations)
print(len(galaxy_locations))
counter = 0 
ans = 0            
for i, pos1 in enumerate(galaxy_locations):
    for j, pos2 in enumerate(galaxy_locations[:i]):
        dist = abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])
        # print(i,j,dist)
        ans += dist  
        counter += 1
print(ans)
# print(counter)