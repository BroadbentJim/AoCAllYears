from copy import deepcopy
D = open("input.txt").readlines()

G = [x.strip() for x in D]

for i, row in enumerate(G):
    pos = row.find("^")
    if pos != -1:
        start_pos = (i,pos)
        break

cur_pos = deepcopy(start_pos)
H,W = len(G), len(G[0])
def is_in_grid(pos):
    return 0<= pos[0] and pos[0] < H and 0 <= pos[1] and pos[1] < W

visited_squares = set()

cur_dir = (-1,0)

while is_in_grid(cur_pos):
    print(cur_pos, cur_dir)
    visited_squares.add(cur_pos)
    new_pos = (cur_pos[0]+cur_dir[0], cur_pos[1]+ cur_dir[1])
    if is_in_grid(new_pos) and G[new_pos[0]][new_pos[1]] == '#':
        cur_dir = (cur_dir[1], -cur_dir[0])
    cur_pos = (cur_pos[0]+cur_dir[0], cur_pos[1]+ cur_dir[1])

print(len(visited_squares))


def is_loop(new_pos):
    G_p = deepcopy(G)
    G_p[new_pos[0]] = G_p[new_pos[0]][:new_pos[1]] + '#' + G_p[new_pos[0]][new_pos[1]+1:]
    assert sum(a != b for a,b in zip(G[new_pos[0]], G_p[new_pos[0]], strict=True)) == 1
    points_n_dirs = set()
    
    cur_pos = start_pos
    cur_dir = (-1,0)

    while is_in_grid(cur_pos) and (cur_pos, cur_dir) not in points_n_dirs:
        # print(cur_pos, cur_dir)
        points_n_dirs.add((cur_pos, cur_dir))
        new_pos = (cur_pos[0]+cur_dir[0], cur_pos[1]+ cur_dir[1])
        if is_in_grid(new_pos) and G_p[new_pos[0]][new_pos[1]] == '#':
            cur_dir = (cur_dir[1], -cur_dir[0])
        else:            
            cur_pos = new_pos
    assert not is_in_grid(cur_pos) or (cur_pos, cur_dir) in points_n_dirs
    return is_in_grid(cur_pos)

ans = 0
for point in visited_squares:
    if point == start_pos:
        continue
    result = is_loop(point)
    # if result:
    #     print(point)
    ans += result
print(ans)
        
        
        