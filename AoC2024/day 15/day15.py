D = open("input.txt").readlines()


G = []
while D[0].strip() != '':
    L = D.pop(0).strip()
    G.append(L)
G = [list(x) for x in G]
for i, row in enumerate(G):
    for j, char in enumerate(row):
        if char == '@':
            start_robot_index = (i,j)
            break

def process_instruction(cur_robot_location: tuple[int,int], current_board: list[list[str]], dir: str) -> tuple[tuple[int,int], list[list[str]]]:
    assert current_board[cur_robot_location[0]][cur_robot_location[1]] == '@'
    tuple_dir: tuple[int,int]
    if dir == '^':
        tuple_dir = (-1,0)
    elif dir == '>':
        tuple_dir = (0,1)
    elif dir == '<':
        tuple_dir = (0,-1)
    elif dir == 'v':
        tuple_dir = (1,0)
    assert tuple_dir
    new_loc = (cur_robot_location[0]+tuple_dir[0],cur_robot_location[1]+tuple_dir[1])
    if current_board[new_loc[0]][new_loc[1]] == '.':
        print("Empty space")
        current_board[new_loc[0]][new_loc[1]] = '@'
        current_board[cur_robot_location[0]][cur_robot_location[1]] = '.'
        return new_loc, current_board    
    elif current_board[new_loc[0]][new_loc[1]] == '#':
        print("Wall")
        # Do nothing
        return cur_robot_location, current_board
    elif current_board[new_loc[0]][new_loc[1]] == 'O':
        print("Hit block")
        # Attempt push block
        wall_loc = new_loc
        newer_loc = (wall_loc[0]+tuple_dir[0],wall_loc[1]+tuple_dir[1])
        while current_board[newer_loc[0]][newer_loc[1]] == 'O':
            newer_loc = (newer_loc[0]+tuple_dir[0],newer_loc[1]+tuple_dir[1])
        if current_board[newer_loc[0]][newer_loc[1]] == '.':
            # Swap the wall at wall loc to sit at newer_loc
            current_board[newer_loc[0]][newer_loc[1]] = 'O'
            # Move the robot into the gap
            current_board[wall_loc[0]][wall_loc[1]] = '@'
            # Remove robot from old spot
            current_board[cur_robot_location[0]][cur_robot_location[1]] = '.'
            return wall_loc, current_board
        elif current_board[newer_loc[0]][newer_loc[1]] == '#':
            # Unsuccessful at pushing the boxes
            return cur_robot_location, current_board
        else:
            pass
    else:
        print("SAD, hit weirdness?")
        print(cur_robot_location, new_loc, dir)
        print(current_board[cur_robot_location[0]][cur_robot_location[1]])
        print(current_board[new_loc[0]][new_loc[1]])

def calculate_GPS_coordinate(box_pos: tuple[int,int]) -> int:
    return 100*box_pos[0] + box_pos[1]


def calculate_score(grid):
    ans = 0
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == 'O':
                ans += calculate_GPS_coordinate((i,j))
    return ans

moves = ''.join(x.strip() for x in D)
# cur_robot_loc = start_robot_index
# cur_board = G
# for move in moves:
#     print(move,cur_robot_loc,)
#     cur_robot_loc, cur_board = process_instruction(cur_robot_loc, cur_board, move)

# print(G)

# ans = calculate_score(G)
# print(ans)

H, W = len(G), len(G[0])
G_2 = [[0 for _ in range(2*W)] for _ in range(H)]

for i,row in enumerate(G):
    for j, char in enumerate(row):
        if char == '.':
            G_2[i][2*j] = '.'
            G_2[i][2*j+1] = '.'
        elif char == '#':
            G_2[i][2*j] = '#'
            G_2[i][2*j+1] = '#'
        elif char == 'O':
            # NB: Important that boxes have a left and a right so we
            # know which other one to move
            G_2[i][2*j] = '['
            G_2[i][2*j+1] = ']'
        elif char == '@':
            G_2[i][2*j] = '@'
            G_2[i][2*j+1] = '.'
        else:
            print("MEWO", char)

print(G_2)            
assert all(all(char != 0 for char in row) for row in G_2)



def process_instruction_2(cur_robot_location: tuple[int,int], current_board: list[list[str]], dir: str) -> tuple[tuple[int,int], list[list[str]]]:
    assert current_board[cur_robot_location[0]][cur_robot_location[1]] == '@'
    tuple_dir: tuple[int,int]
    if dir == '^':
        tuple_dir = (-1,0)
    elif dir == '>':
        tuple_dir = (0,1)
    elif dir == '<':
        tuple_dir = (0,-1)
    elif dir == 'v':
        tuple_dir = (1,0)
    assert tuple_dir
    new_loc = (cur_robot_location[0]+tuple_dir[0],cur_robot_location[1]+tuple_dir[1])
    if current_board[new_loc[0]][new_loc[1]] == '.':
        print("Empty space")
        current_board[new_loc[0]][new_loc[1]] = '@'
        current_board[cur_robot_location[0]][cur_robot_location[1]] = '.'
        return new_loc, current_board    
    elif current_board[new_loc[0]][new_loc[1]] == '#':
        print("Wall")
        # Do nothing
        return cur_robot_location, current_board
    elif current_board[new_loc[0]][new_loc[1]] == '[':
        print("Hit block: left")
        if tuple_dir[0] != 0:
            succeeded, current_board = process_push_wide_block_vertically((new_loc[0],new_loc[1]), current_board, tuple_dir)
        else:
            succeeded, current_board = process_push_wide_block_horizontally((new_loc[0],new_loc[1]), current_board, tuple_dir)
        if succeeded:
            assert current_board[new_loc[0]][new_loc[1]] == '.'
            current_board[new_loc[0]][new_loc[1]] = '@'
            current_board[cur_robot_location[0]][cur_robot_location[1]] = '.'
            return new_loc, current_board
        else:
            return cur_robot_location, current_board
    elif current_board[new_loc[0]][new_loc[1]] == ']':
        print("Hit block: right")
        assert new_loc[1] >= 3, "Need new_loc[1]-1 in grid"
        if tuple_dir[0] != 0:
            succeeded, current_board = process_push_wide_block_vertically((new_loc[0],new_loc[1]-1), current_board, tuple_dir)
        else:
            succeeded, current_board = process_push_wide_block_horizontally((new_loc[0],new_loc[1]), current_board, tuple_dir)
        if succeeded:
            assert current_board[new_loc[0]][new_loc[1]] == '.'
            current_board[new_loc[0]][new_loc[1]] = '@'
            current_board[cur_robot_location[0]][cur_robot_location[1]] = '.'
            return new_loc, current_board
        else:
            return cur_robot_location, current_board
    else:
        print("SAD, hit weirdness?")
        print(cur_robot_location, new_loc, dir)
        print(current_board[cur_robot_location[0]][cur_robot_location[1]])
        print(current_board[new_loc[0]][new_loc[1]])
        
        
def process_push_wide_block_vertically(left_block_coords: tuple[int,int], current_board: list[list[int]], cur_dir: tuple[int,int]) -> tuple[bool, list[list[int]]]:
    # left_block_coords always represents the coords of the left block

    # Try a stack
    # Left blocks of things to check
    blocks_to_check = [left_block_coords]
    # Places to insert new blocks
    blocks_to_move = []
    # print(cur_dir)
    while blocks_to_check:
        # print("1", blocks_to_check, blocks_to_move)
        block = blocks_to_check.pop()
        # Check left
        new_loc = (block[0]+cur_dir[0], block[1]+cur_dir[1])
        new_value = current_board[new_loc[0]][new_loc[1]]
        # print(new_loc, new_value)
        if new_value == '.':
            pass
        elif new_value == '#':
            return False, current_board
        elif new_value == '[':
            blocks_to_check.append(new_loc)
        elif new_value == ']':
            assert current_board[new_loc[0]][new_loc[1]-1] == '['
            
            blocks_to_check.append((new_loc[0], new_loc[1]-1))
        # Check right
        new_loc = (block[0]+cur_dir[0], block[1]+cur_dir[1]+1)
        new_value = current_board[new_loc[0]][new_loc[1]]
        if new_value == '.':
            pass
        elif new_value == '#':
            return False, current_board
        elif new_value == '[':
            blocks_to_check.append(new_loc)
        elif new_value == ']':
            # This case is already handled
            # Represents a block sitting directly on top of this one
            assert current_board[new_loc[0]][new_loc[1]-1] == '['
            pass
        blocks_to_move.insert(0,(block[0]+cur_dir[0], block[1]+cur_dir[1]))
    blocks_already_moved = set()
    for block in blocks_to_move:
        print(block)
        if block in blocks_already_moved:
            continue
        assert current_board[block[0]][block[1]:block[1]+2] == ['.','.'], current_board[block[0]][block[1]:block[1]+2]
        current_board[block[0]][block[1]] = '['
        current_board[block[0]][block[1]+1] = ']'
        current_board[block[0]-cur_dir[0]][block[1]] = '.'
        current_board[block[0]-cur_dir[0]][block[1]+1] = '.'
        blocks_already_moved.add(block)
    return True, current_board
        
def process_push_wide_block_horizontally(block_coords, current_board, cur_dir) -> tuple[bool, list[list[int]]]:
    # If going left, block_coords == ]
    # If going right,
    assert current_board[block_coords[0]][block_coords[1]] in '[]'
    assert cur_dir in [(0,1), (0,-1)]
    assert cur_dir == (0,1) and current_board[block_coords[0]][block_coords[1]] == '[' or (cur_dir == (0,-1) and current_board[block_coords[0]][block_coords[1]] == ']')
    
    # Find how many sideways are still []
    cur_block_coords = block_coords
    blocks_to_move = []
    # print("HERE", current_board[cur_block_coords[0]][cur_block_coords[1]])
    while current_board[cur_block_coords[0]][cur_block_coords[1]] in '[]':
        blocks_to_move.insert(0,cur_block_coords)
        cur_block_coords = (cur_block_coords[0], cur_block_coords[1]+2*cur_dir[1])
    final_value = current_board[cur_block_coords[0]][cur_block_coords[1]]
    # print(final_value)
    if final_value == '#':
        return False, cur_board
    elif final_value == '.':
        # print(blocks_to_move)
        for block in blocks_to_move:
            # print(block, {cur_board[block[0]][block[1]+0*cur_dir[1]], cur_board[block[0]][block[1]+1*cur_dir[1]]})
            assert {cur_board[block[0]][block[1]+0*cur_dir[1]], cur_board[block[0]][block[1]+1*cur_dir[1]]} == {'[',']'}
            assert cur_board[block[0]][block[1]+2*cur_dir[1]] == '.'
            # assert
            cur_board[block[0]][block[1]+2*cur_dir[1]] = cur_board[block[0]][block[1]+cur_dir[1]]
            cur_board[block[0]][block[1]+cur_dir[1]] = cur_board[block[0]][block[1]]    
            cur_board[block[0]][block[1]] = '.'
        return True, cur_board
    else:
        print("ASD")
        raise Exception
    
for i, row in enumerate(G_2):
    for j, char in enumerate(row):
        if char == '@':
            start_robot_index = (i,j)
            break

def render_board(board):
    for row in board:
        print("".join(row))
                
cur_robot_loc = start_robot_index
cur_board = G_2
print(len(moves))
for i, move in enumerate(moves):
    # print(move,cur_robot_loc,)
    # if i > 6970:
    #     render_board(cur_board)
    print(i,move, cur_robot_loc)
    cur_robot_loc, cur_board = process_instruction_2(cur_robot_loc, cur_board, move)
    

render_board(G_2)

def calculate_score_2(grid):
    ans = 0
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == '[':
                ans += calculate_GPS_coordinate((i,j))
    return ans


ans = calculate_score_2(G_2)
print(ans)