from collections import defaultdict
from dataclasses import dataclass

@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int
INPUT = 1364
# INPUT = 10
TARGET = Coordinate(x=31,y=39)
# TARGET = Coordinate(x=7,y=4)
START_LOC = Coordinate(x=1,y=1)
# Methodology
# Store a dictionary of whether tile is filled

def calculate_is_wall(coordinate: Coordinate) -> bool:
    x,y = coordinate.x, coordinate.y
    if x < 0 or y < 0:
        return True
    algebraic_exp = x**2  + 3*x + 2*x*y+ y +y**2
    algebraic_exp += INPUT
    bin_exp = bin(algebraic_exp)
    ones_count = bin_exp[2:].count("1")
    return ones_count % 2

def heuristic(current: Coordinate) -> int:
    diff_x = abs(TARGET.x-current.x)
    diff_y = abs(TARGET.y-current.y)
    return diff_x + diff_y

GRID: dict[Coordinate, bool] = {}
openSet: set[Coordinate] = set([START_LOC])


def handle_new_square(source: Coordinate, new_square: Coordinate):
    if new_square not in GRID:
        is_wall = calculate_is_wall(new_square)
        GRID[new_square] = is_wall
    is_wall = GRID[new_square]
    if not is_wall:
        tentative_gScore = gScore[source] + 1
        if tentative_gScore < gScore[new_square]:
            gScore[new_square] = tentative_gScore
            fScore[new_square] = tentative_gScore + heuristic(new_square)
            if new_square not in openSet:
                openSet.add(new_square)

def traverse(cur_coordinate: Coordinate):
    go_left = Coordinate(cur_coordinate.x-1, cur_coordinate.y)
    go_up = Coordinate(cur_coordinate.x, cur_coordinate.y+1)
    go_right = Coordinate(cur_coordinate.x+1, cur_coordinate.y)
    go_down = Coordinate(cur_coordinate.x, cur_coordinate.y-1)
    new_squares = [go_left, go_up, go_right, go_down]
    any(map(lambda x : handle_new_square(cur_coordinate, x), new_squares))

gScore = defaultdict(lambda: float('inf'))
fScore = defaultdict(lambda: float('inf'))
gScore[START_LOC] = 0
fScore[START_LOC] = heuristic(START_LOC)
# pt1: A8 star algo
while openSet:
    cur_coordinate = sorted(openSet, key=lambda coord: fScore[coord])[0]
    if cur_coordinate == TARGET:
        print("REACHED TARGET")
        print(fScore[cur_coordinate])
        break
    openSet.remove(cur_coordinate)
    traverse(cur_coordinate)
        
# print(GRID)
# print("=" * 60)
# print(has_visited)

# pt2: BFS
# Need to store for each vertex the shortest path to that vertex
# Then continue searching
MAX_DIST = 50
shortest_path: dict[Coordinate, int] = defaultdict(lambda: float('inf'))
shortest_path[START_LOC] = 0
openSet: set[Coordinate] = {START_LOC}

"""
while openSet:
    get element from openSet of shortest distance from origin
    add all neighbors to shortest_path with dist <= MAX_DIST, adjusting their shortest path if necessary
    if we adjust their shortest path, add them into openSet
    Remove current node from openSet. Will be added back later if we find a faster path
"""
def BFS_handle_new_square(prev_dist: int, new_square: Coordinate):
    if new_square not in GRID:
        is_wall = calculate_is_wall(new_square)
        GRID[new_square] = is_wall
    is_wall = GRID[new_square]
    if is_wall:
        return
    candidate_new_dist = prev_dist + 1
    if candidate_new_dist > MAX_DIST:
        return
    if candidate_new_dist < shortest_path[new_square]:
        shortest_path[new_square] = candidate_new_dist
        openSet.add(new_square)
    
def BFS_traverse(cur_coordinate: Coordinate):
    cur_distance = shortest_path[cur_coordinate]
    go_left = Coordinate(cur_coordinate.x-1, cur_coordinate.y)
    go_up = Coordinate(cur_coordinate.x, cur_coordinate.y+1)
    go_right = Coordinate(cur_coordinate.x+1, cur_coordinate.y)
    go_down = Coordinate(cur_coordinate.x, cur_coordinate.y-1)
    new_squares = [go_left, go_up, go_right, go_down]
    list(map(lambda x : BFS_handle_new_square(cur_distance, x), new_squares))

while openSet:
    cur_coordinate =  sorted(openSet, key= lambda coord: shortest_path[coord])[0]
    openSet.remove(cur_coordinate)
    BFS_traverse(cur_coordinate)

assert all([x <= 50 for x in shortest_path.values()])
print(len(shortest_path))
    

