D = open("input.txt").readlines()
L = [l.strip() for l in D]

W = len(L[0])
H = len(L)
L = ["." + l + "." for l in L]
L.insert(0, "."* (W+2))
L.append("."* (W+2))

OG_grid = L
print(len(OG_grid), len(OG_grid[0]))
def count_nieghbors(grid: list[list[str]], i,j: int) -> int:
    first_seg = grid[i-1][j-1:j+2].count("#")
    middle_seg = (grid[i][j-1] + grid[i][j+1]).count("#")
    final_seg = grid[i+1][j-1:j+2].count("#")
    return first_seg + middle_seg + final_seg

# print(OG_grid[1][3])
# print(count_nieghbors(OG_grid, i=1, j=3))

def next_value(grid: list[list[str]], i,j: int) -> str:
    cur_val = grid[i][j]
    neighs = count_nieghbors(grid, i,j)
    assert 0 <= neighs and neighs <= 8
    assert cur_val in ["#", "."]
    if cur_val == "#" and neighs in [2,3] or cur_val == "." and neighs == 3:
        return "#"
    else:
        return "."
    
def process_grid(grid: list[list[str]]) -> list[list[str]]:
    new_grid = [["."]*(W+2) for _ in range(H+2)]
    # print(len(new_grid), len(new_grid[0]))
    for i in range(1, W+1):
        for j in range(1, H+1):
            new_val = next_value(grid, i,j)
            new_grid[i][j] = new_val
    return new_grid

T = 100
# # for row in OG_grid:
# #     print(row)    
# working_grid = OG_grid
# for _ in range(T):
#     # print("=" * (8*W))
#     new_grid = process_grid(working_grid)
#     working_grid = new_grid
#     # for row in working_grid:
#     #     print(row)    

# pt2 
T = 100
working_grid = [list(x) for x in OG_grid]
working_grid[1][1] = "#"
working_grid[1][W] = "#"
working_grid[H][1] = "#"
working_grid[H][W] = "#"
for _ in range(T):
    # print("=" * (8*W))
    new_grid = process_grid(working_grid)
    new_grid[1][1] = "#"
    new_grid[1][W] = "#"
    new_grid[H][1] = "#"
    new_grid[H][W] = "#"
    working_grid = new_grid
    # for row in working_grid:
    #     print(row)    
count_elements = sum(x.count("#") for x in working_grid)
print(count_elements)