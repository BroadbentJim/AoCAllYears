D = open("input.txt").readlines()

# G = ['.' + x.strip() + '.' for x in D]
# G = ['.'*len(G[0])] + G + ['.'*len(G[0])]
G = [x.strip() for x in D]
H,W = len(G),len(G[0])
print(G)



def is_in_grid(pos):
    return 0<= pos[0] and pos[0] < H and 0 <= pos[1] and pos[1] < W


# seen_already: set[tuple[int,int]] = set()
# def do_bfs(cur_char: str, cur_coord: tuple[int,int]) -> tuple[int,int]:
#     assert cur_char != '.'
#     seen_already.add(cur_coord)
#     area = 1
#     perimeter = 0
#     extra_area = 0
#     extra_perimeter = 0
#     for dir in [(1,0), (-1,0), (0,1), (0,-1)]:
#         new_point = (cur_coord[0]+dir[0], cur_coord[1]+dir[1])
#         if not is_in_grid(new_point):
#             perimeter += 1
#             continue
#         new_char = G[new_point[0]][new_point[1]]        
#         if (new_point not in seen_already and new_char == cur_char):
#             new_area, new_perimeter = do_bfs(cur_char, new_point)
#             extra_area += new_area
#             extra_perimeter += new_perimeter
#         if new_char != cur_char:
#             perimeter += 1
#     return area+extra_area, perimeter+extra_perimeter
                
# ans = 0
# for i, row in enumerate(G):
#     for j, char in enumerate(row):
#         if (i,j) in seen_already or char == '.':
#             continue
#         area, perimeter = do_bfs(char, (i,j))
#         print(char, area, perimeter)
#         ans += area * perimeter
# assert len(seen_already) == (H)*(W)
# print(ans) 
        
        
seen_already: set[tuple[int,int]] = set()
def do_bfs_find_perimeter(cur_char: str, cur_coord: tuple[int,int], set_perimeter: set[tuple[int,int]]) -> tuple[int,int]:
    assert cur_char != '.'
    seen_already.add(cur_coord)
    area = 1
    perimeter = 0
    extra_area = 0
    extra_perimeter = 0
    for dir in [(1,0), (-1,0), (0,1), (0,-1)]:
        new_point = (cur_coord[0]+dir[0], cur_coord[1]+dir[1])
        if not is_in_grid(new_point):
            perimeter += 1
            continue
        new_char = G[new_point[0]][new_point[1]]        
        if (new_point not in seen_already and new_char == cur_char):
            new_area, new_perimeter = do_bfs_find_perimeter(cur_char, new_point, set_perimeter)
            extra_area += new_area
            extra_perimeter += new_perimeter
        if new_char != cur_char:
            perimeter += 1
    if perimeter != 0:
        set_perimeter.add(cur_coord)
    return area+extra_area, perimeter+extra_perimeter


DIRS = [(1,0), (0,-1), (-1,0), (0,1)]

def traverse_perimeter(cur_char:str, cur_coord: tuple[int,int], cur_dir_index: int, visited_perimeter: set[tuple[tuple[int,int],int]], actual_perimeter: set[int,int]) -> int:
    cur_dir = DIRS[cur_dir_index]
    print("MID", cur_char, cur_coord, cur_dir, cur_dir_index, visited_perimeter, set_perimeter)
    if (cur_coord, cur_dir_index) in visited_perimeter:
        return 0
    visited_perimeter.add((cur_coord, cur_dir_index))
    
    new_point = (cur_coord[0]+cur_dir[0], cur_coord[1]+cur_dir[1])
    
    if is_in_grid(new_point) and new_point in actual_perimeter:
        # assert new_point in actual_perimeter
        return traverse_perimeter(cur_char, new_point, cur_dir_index, visited_perimeter, actual_perimeter)
    
    if not is_in_grid(new_point) or new_point not in actual_perimeter:
        # assert G[new_point[0]][new_point[1]] != cur_char
        new_dir_index, turns = acquire_new_direction(cur_coord, cur_dir_index, visited_perimeter)
        # if (cur_coord, new_dir_index) in visited_perimeter:
        #     print("SCARY")
        #     return turns
        new_dir = DIRS[new_dir_index]
        print(cur_char, new_dir, turns)
        # newer_point = (cur_coord[0]+new_dir[0], cur_coord[1]+new_dir[1])
        new_turns = traverse_perimeter(cur_char, cur_coord, new_dir_index, visited_perimeter, actual_perimeter)
        turns += new_turns
        return turns
        
    
def acquire_new_direction(start_coord, start_dir_index, visited_perimeter: set[tuple[tuple[int,int],int]]) -> tuple[int,int]:
    if visited_perimeter is None:
        visited_perimeter = set()
    start_char = G[start_coord[0]][start_coord[1]]
    cur_dir_index = start_dir_index
    cur_dir = DIRS[cur_dir_index]
    new_point = (start_coord[0]+cur_dir[0], start_coord[1]+cur_dir[1])
    turns = 0
    while not is_in_grid(new_point) or (G[new_point[0]][new_point[1]], cur_dir_index) in visited_perimeter:
        visited_perimeter.add((start_coord, cur_dir_index))
        cur_dir_index += 1
        cur_dir_index %= len(DIRS)
        turns += 1
        if (start_coord, cur_dir_index) in visited_perimeter:
            break
        if cur_dir_index == 3:
            print("UADS")
        cur_dir = DIRS[cur_dir_index]
        new_point = (start_coord[0]+cur_dir[0], start_coord[1]+cur_dir[1])
    return cur_dir_index, turns

                
ans = 0
for i, row in enumerate(G):
    for j, char in enumerate(row):
        if (i,j) in seen_already or char == '.':
            continue
        set_perimeter = set()
        area, perimeter = do_bfs_find_perimeter(char, (i,j), set_perimeter)
        assert 0< len(set_perimeter) <= perimeter
        start_coord = next(iter(set_perimeter))
        start_char = G[start_coord[0]][start_coord[1]]
        if start_char != 'C':
            continue
        visited_perimeter = set()
        start_dir_index = 0
        cur_dir_index, turns = acquire_new_direction(start_coord, start_dir_index, None)
        print("STARTING", start_char, start_coord, cur_dir_index, visited_perimeter, set_perimeter, turns)
        print("Start Coord", start_coord, "Start dir", DIRS[cur_dir_index])
        if turns != 4:
            turns = traverse_perimeter(start_char, start_coord, cur_dir_index, visited_perimeter, set_perimeter)
        print("TURNS", turns)
        ans += area * turns
assert len(seen_already) == (H)*(W)
print(ans) 