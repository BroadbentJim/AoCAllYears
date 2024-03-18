D = open("input.txt").readlines()

moves = D[0].strip().split(", ")
print(moves)

cur_pos = (0,0)
cur_dir = "N"
loc_has_visited = set()
loc_has_visited.add((0,0))
assert (0,0) in loc_has_visited
def process_move(cur_pos, cur_dir, move):
    turn = move[0]
    new_dir = None
    match cur_dir:
        case "N":
            if turn == "R":
                new_dir = "E"
            elif turn == "L":
                new_dir = "W"
        case "E":
            if turn == "R":
                new_dir = "S"
            elif turn == "L":
                new_dir = "N"
        case "S":
            if turn == "R":
                new_dir = "W"
            elif turn == "L":
                new_dir = "E"
        case "W":
            if turn == "R":
                new_dir = "N"
            elif turn == "L":
                new_dir = "S"
        case _:
            print(f"{turn=}")
    steps = int(move[1:])
    match new_dir:
        case "N":
            visited = [(cur_pos[0], cur_pos[1]+i) for i in range(1,steps+1)]            
            new_pos = (cur_pos[0], cur_pos[1]+steps)
        case "E":
            visited = [(cur_pos[0]+i, cur_pos[1]) for i in range(1,steps+1)]
            new_pos = (cur_pos[0]+steps, cur_pos[1])
        case "S":
            visited = [(cur_pos[0], cur_pos[1]-i) for i in range(1,steps+1)]
            new_pos = (cur_pos[0], cur_pos[1]-steps)
        case "W":
            visited = [(cur_pos[0]-i, cur_pos[1]) for i in range(1,steps+1)]
            new_pos = (cur_pos[0]-steps, cur_pos[1])
        case _:
            print(f"{new_dir=}")
    for pos in visited:
        if pos in loc_has_visited:
            print("REACHED")
            return pos, False
        loc_has_visited.add(pos)
    return new_pos, new_dir

for move in moves:
    print(move, cur_pos, cur_dir)
    cur_pos, cur_dir = process_move(cur_pos, cur_dir, move)
    if not cur_dir:
        break
print(cur_pos)
print(sum(map(abs, cur_pos)))
# print(loc_has_visited)