from copy import deepcopy
D = open("input18.txt").read().splitlines()

tot_right = 0
tot_down = 0
for line in D:
    dir, length, color = line.split()
    # print(dir, length)
    if dir == "R":
        tot_right += int(length)
    elif dir == 'D':
        tot_down += int(length)

grid =[["." for _ in range(tot_right+1)] for _ in range(tot_down+1)]

cur_pos = [0,0]
for line in D:
    # print(cur_pos)
    dir, length, color = line.split()
    length = int(length)
    match dir:
        case "R":
            for i in range(cur_pos[1], cur_pos[1]+length):
                grid[cur_pos[0]][i] = "#"
            cur_pos[1] += length
        case "L":
            for i in range(cur_pos[1], cur_pos[1]-length,-1):
                # print(cur_pos[0], i)
                grid[cur_pos[0]][i] = "#"
            cur_pos[1] -= length
        case "U":
            for i in range(cur_pos[0], cur_pos[0]-length,-1):
                grid[i][cur_pos[1]] = "#"
            cur_pos[0] -= length
        case "D":
            for i in range(cur_pos[0], cur_pos[0]+length):
                grid[i][cur_pos[1]] = "#"
            cur_pos[0] += length

# for row in grid:
#     print(row)

# Pad the grid
W = len(grid[0])
grid = [['.'] * W] + grid + [['.'] * W]
grid = [["."] + x + ["."] for x in grid]
H = len(grid)
W = len(grid[0])
print(f"H: {H}, W: {W}")
for row in grid:
    print(row)

# def check_slice(grid_slice):
#     if len(grid_slice) == 0:
#         return False
#     num_hash_lines = 0
#     cur_char = grid_slice[0]
#     for char in grid_slice[1:]:
#         if char == '.' and cur_char == '#':
#             num_hash_lines += 1
#         cur_char = char    
#     return num_hash_lines % 2

def check_slice(grid_slice):
    if len(grid_slice) == 0:
        return False
    num_hashs = 0
    last_hash = -1
    in_hash = False
    for i,char in enumerate(grid_slice[1:]):
        if char == '.' and in_hash:
            if i-last_hash == 1:
                num_hashs += 1
        elif char == '#' and not in_hash:
            last_hash = i
            in_hash = True
    
    return num_hashs
        
    


new_grid = deepcopy(grid)
for i, row in enumerate(grid):
    if i in [0, H-1]:
        continue
    for j, char in enumerate(row):
        if j in [0,W-1]:
            continue
        if char == "#":
            continue
        # A point lies in the interior against a wall if when you go out in the opposite direction
        # you cross a path of #'s an odd number of times
        is_interior = []
        for o_x, o_y in [[0,1],[1,0],[-1,0],[0,-1]]:
            # x,y = i+o_x, j+o_y
            # print(i,j, x,y)
            # Check the other direction crossing number
            match (o_x,o_y):
                case (0,1):
                    grid_slice = grid[i][:j+1]
                case (1,0):
                    grid_slice = [grid[l][j] for l in range(i+1)]
                case (-1,0):
                    grid_slice = [grid[l][j] for l in range(i,H)]
                case (0,-1):
                    grid_slice = grid[i][j:]
            # print(grid_slice)
            interior_point = check_slice(grid_slice)
            # print(interior_point)
            is_interior.append(interior_point)
        # print(i,j,is_interior)
        if sum(is_interior) >= 4:
            new_grid[i][j] = '#'
            
print("-" * W*5)                    
ans = 0
for row in new_grid:
    print(row)
    ans += row.count("#")    
print(ans)
