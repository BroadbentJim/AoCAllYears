from copy import deepcopy
D = open("input14.txt").read().splitlines()

#Iterate along columns
#From north to south, have boulders roll

#Do I wanna invert and move to a columnar format
def roll_boulders_north(col_grid):
    for i,col in enumerate(col_grid):
        cur_lowest = 0
        new_col = col
        for j, char in enumerate(new_col):
            if char == ".":
                continue
            elif char == "#":
                cur_lowest = j+1
            elif char == 'O' and j != cur_lowest:
                new_col[cur_lowest] = "O"
                new_col[j] = '.'
                cur_lowest += 1
            elif char == 'O' and j == cur_lowest:
                cur_lowest += 1
            else:
                print(j, char, "UNDEFINED")
        col_grid[i] = new_col
    return col_grid

# def rotate_columnar_grid_anticlockwise(col_grid):
#     # with col, row
#     # i,j -> j, -i
#     H = len(col_grid[0])
#     W = len(col_grid)
#     rot_col_grid = [[x[j] for x in reversed(col_grid)] for j in range(W)]
#     return rot_col_grid
    
def rotate_columnar_grid_clockwise(col_grid):
    # with col,row
    # i,j -> -j,i
    W = len(col_grid)
    rot_col_grid = [[x[j] for x in col_grid]for j in range(W-1,-1,-1)]
    return rot_col_grid

def do_cycle(col_grid):
    for j in range(4):
        # row_lines = [[x[j] for x in col_grid] for j in range(len(D[0]))]
        # for line in row_lines:
        #     print(line)
        # print(j)
        col_grid = roll_boulders_north(col_grid)
        col_grid = rotate_columnar_grid_clockwise(col_grid)
    return col_grid
col_lines = [[x[j] for x in D] for j in range(len(D[0]))]

# col_lines = roll_boulders_north(col_lines)

def calculate_north_load(col_grid):
    H = len(col_grid[0])
    load = 0
    for col in col_lines:
        for j, char in enumerate(col):
            if char == "O":
                load += H-j
    return load

def find_period(col_grid):
    prev_values = []
    prev_values.append(col_grid)
    new_col_grid = deepcopy(col_grid)
    new_col_grid = do_cycle(new_col_grid)
    # print(starting_value, new_col_grid)
    cur_iter = 1
    while cur_iter < 1e3:
        new_col_grid = deepcopy(new_col_grid)
        new_col_grid = do_cycle(new_col_grid)
        for i,old_grid in enumerate(prev_values):
            if new_col_grid == old_grid:
                # print(prev_values)
                return i, cur_iter
        prev_values.append(new_col_grid)
        cur_iter += 1
start_loop, end_loop =  find_period(col_lines)

period = end_loop-start_loop

remaining = 1000000000 - start_loop
remaining %= period    

for _ in range(start_loop + remaining):
    col_lines = do_cycle(col_lines)

ans = calculate_north_load(col_lines)
print(ans)