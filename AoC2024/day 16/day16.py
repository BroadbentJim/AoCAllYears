from collections import defaultdict
from dataclasses import dataclass

@dataclass(frozen=True)
class ReindeerPos:
    x_pos: int
    y_pos: int
    x_dir: int
    y_dir: int

D = open("input.txt").readlines()

G = [x.strip() for x in D]

for i, row in enumerate(G):
    e_pos = row.find('E')
    if e_pos != -1:
        end_pos = (i,e_pos)
    s_pos = row.find('S')
    if s_pos != -1:
        start_pos = (i,s_pos)

print(start_pos, end_pos)
G = [list(x) for x in G]

# PT1 A*

def heuristic(cur_pos: ReindeerPos) -> int:
    # Manhattan distance
    return abs(end_pos[0] -cur_pos.y_pos) + abs(end_pos[0]- cur_pos.x_pos)

def get_neighbors(cur_pos: ReindeerPos) -> list[tuple[ReindeerPos, int]]:
    # Forwards:
    neighbors = []
    forward_pos = (cur_pos.y_pos + cur_pos.y_dir, cur_pos.x_pos + cur_pos.x_dir)
    if G[forward_pos[0]][forward_pos[1]] != '#':
        forward_reindeer = ReindeerPos(y_pos=forward_pos[0],x_pos=forward_pos[1],y_dir=cur_pos.y_dir, x_dir=cur_pos.x_dir)
        neighbors.append((forward_reindeer, 1))
    # Clockwise
    clockwise_pos = ReindeerPos(y_pos=cur_pos.y_pos,x_pos=cur_pos.x_pos,y_dir=cur_pos.x_dir, x_dir=-cur_pos.y_dir)
    neighbors.append((clockwise_pos, 1000))
    # Anticlockwise
    anti_clockwise_pos = ReindeerPos(y_pos=cur_pos.y_pos,x_pos=cur_pos.x_pos,y_dir=-cur_pos.x_dir, x_dir=cur_pos.y_dir)
    neighbors.append((anti_clockwise_pos, 1000))
    return neighbors
        

def A_star(start):
    open_set: set[ReindeerPos] = {start}
    
    g_score = defaultdict(lambda: float('inf'))
    g_score[start] = 0
    
    f_score = defaultdict(lambda: float('inf'))
    f_score[start] = heuristic(start)
    came_from = defaultdict(list[ReindeerPos])
    
    while open_set:
        # print(open_set)
        min_f_score = float('inf')
        for cand in open_set:
            if f_score[cand] < min_f_score:
                min_f_score = f_score[cand]
                current = cand
        open_set.remove(current)
        neighbors = get_neighbors(current)
        for neighbor in neighbors:
            neighbor_pos, neighbor_distance = neighbor
            tentative_gScore = g_score[current] + neighbor_distance
            if tentative_gScore <= g_score[neighbor_pos]:
                if tentative_gScore < g_score[neighbor_pos]:
                    came_from[neighbor_pos] = []
                came_from[neighbor_pos].append(current)
                g_score[neighbor_pos] = tentative_gScore
                f_score[neighbor_pos] = tentative_gScore + heuristic(neighbor_pos)
                if neighbor_pos not in open_set:
                    open_set.add(neighbor_pos)
                    
    return g_score, came_from

reindeer_start_pos = ReindeerPos(y_pos=start_pos[0],x_pos=start_pos[1], x_dir=1, y_dir=0)                
g_scores, came_from = A_star(reindeer_start_pos)
end_positions = [ReindeerPos(y_pos=end_pos[0], x_pos=end_pos[1], x_dir=x[0],y_dir=x[1]) for x in [(1,0), (0,1), (-1,0), (0,-1)]]
ans = min(g_scores[pos] for pos in end_positions)
print(ans)


# PT2
# print(came_from)
def traverse_came_from(g_scores: dict[ReindeerPos, int], came_from: dict[ReindeerPos, list[ReindeerPos]], end_pos: tuple[int,int], start_pos: ReindeerPos) -> set[ReindeerPos]:
    sits_on_winning_path : set[ReindeerPos] = set()
    def recurse(cur_pos):
        sits_on_winning_path.add(cur_pos)
        for previous in came_from[cur_pos]:
            if previous not in sits_on_winning_path:
                recurse(previous)
    
    for end_pos in end_positions:
        if g_scores[end_pos] == ans:
            recurse(end_pos)
    return sits_on_winning_path

def render_board(board):
    for row in board:
        print("".join(row))

sits_on_winner = traverse_came_from(g_scores, came_from, end_pos, start_pos)

indices = {(pos.y_pos, pos.x_pos) for pos in sits_on_winner}
print(len(indices))

# G_p = G
# for y,x in indices:
#     if G_p[y][x] == '.':
#         G_p[y][x] = 'O'
# render_board(G_p)
    