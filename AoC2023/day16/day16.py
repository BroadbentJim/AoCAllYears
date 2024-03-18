from collections import defaultdict
from copy import deepcopy

D = open("input16.txt").read().splitlines()

# DFS
H = len(D)
W = len(D[0])
print(H,W)


def go_through(cur_pos, dir):
    new_pos = cur_pos
    match dir:
        case "R":
            new_pos[1] +=1
        case "L":
            new_pos[1] -= 1
        case "D":
            new_pos[0] += 1
        case "U":
            new_pos[0] -= 1
    new_trajectory = (new_pos, dir)
    return new_trajectory

def process_path(trajectory, prev_processed, count_visited, stack):
    cur_pos = trajectory[0]
    # If OOB, remove this trajectory from the stack
    if cur_pos[0] < 0 or cur_pos[0] >= H or cur_pos[1] < 0 or cur_pos[1] >= W:
        # stack.pop()
        return False
    hash = (cur_pos[0], cur_pos[1], trajectory[1])
    if hash in prev_processed:
        return False
    count_visited[tuple(cur_pos)] += 1
    dir = trajectory[1]
    # print(cur_pos)
    cur_tile = D[cur_pos[0]][cur_pos[1]]
    match cur_tile:
        case ".":
            return go_through(cur_pos, dir)
        case "|":
            if dir in ["U", "D"]:
                return go_through(cur_pos, dir)
            else:
                top_path = ([cur_pos[0]-1, cur_pos[1]], "U")
                bot_path = ([cur_pos[0]+1, cur_pos[1]], "D")
                stack.append(top_path)
                stack.append(bot_path)
                return False
        case "-":
            if dir in ["L", "R"]:
                return go_through(cur_pos, dir)
            else:
                left_path = ([cur_pos[0], cur_pos[1]-1], "L")
                right_path = ([cur_pos[0], cur_pos[1]+1], "R")
                stack.append(left_path)
                stack.append(right_path)
                return False
        case "/":
            new_pos = cur_pos
            match dir:                
                case "L":
                    new_dir = "D"
                    new_pos[0] += 1
                    return (new_pos, new_dir)
                case "R":
                    new_dir = "U"
                    new_pos[0] -= 1
                    return (new_pos, new_dir)
                case "U":
                    new_dir = "R"
                    new_pos[1] += 1
                    return (new_pos, new_dir)
                case "D":
                    new_dir = "L"
                    new_pos[1] -= 1
                    return (new_pos, new_dir)
        case "\\":
            new_pos = cur_pos
            match dir:
                case "L":
                    new_dir = "U"
                    new_pos[0] -= 1
                    return (new_pos, new_dir)
                case "R":
                    new_dir = "D"
                    new_pos[0] += 1
                    return (new_pos, new_dir)
                case "U":
                    new_dir = "L"
                    new_pos[1] -= 1
                    return (new_pos, new_dir)
                case "D":
                    new_dir = "R"
                    new_pos[1] += 1
                    return (new_pos, new_dir)
        case _:
            print("ERROR")
            

def simulate_beam_trajectory(initial_trajectory):
    count_visited = defaultdict(int)
    stack = []
    stack.append(initial_trajectory)
    prev_processed = set()
    i = 0
    while stack:
        # print(stack, len(stack))
        # print(len(stack))
        # print(count_visited)
        og_trajectory = stack.pop(0)
        og_hash = (og_trajectory[0][0], og_trajectory[0][1], og_trajectory[1])
        cur_trajectory = deepcopy(og_trajectory)
        
        while cur_trajectory:
            cur_trajectory = process_path(cur_trajectory, prev_processed, count_visited, stack)
        prev_processed.add(og_hash)
        i += 1
    ans = sum(x >= 1 for x in count_visited.values())
    return ans


cur_max = simulate_beam_trajectory(([0,0], "R"))

for i in range(W):
    incid_pos = [0, i]
    new = simulate_beam_trajectory((incid_pos, "D"))
    cur_max = max(cur_max, new)
    
for i in range(W):
    incid_pos = [H-1, i]
    new = simulate_beam_trajectory((incid_pos, "U"))
    cur_max = max(cur_max, new)
    
for j in range(H):
    incid_pos = [j,0]
    new = simulate_beam_trajectory((incid_pos, "R"))
    cur_max = max(cur_max, new)

for j in range(H):
    incid_pos = [j,W-1]
    new = simulate_beam_trajectory((incid_pos, "L"))
    cur_max = max(cur_max, new)
    
print(cur_max)
