from hashlib import md5
from collections import defaultdict
from dataclasses import dataclass
INPUT = "bwnlcvfs"
TARGET = (3,3)
ALLOWED_CHARS = ["b", "c", "d", "e", "f"]
N = len(INPUT)
"""
Methodology:
BFS. Need to keep track of the path taken, but really shouldn't be that bad
"""

W = 3
H = 3

@dataclass(frozen=True)
class VertexInfo:
    path: str
    coords: tuple[int,int]
    available_dirs: tuple[bool,bool,bool,bool]

def get_allowed_dirs(path: str) -> tuple[bool,bool,bool,bool]:
    keys = md5(path.encode()).hexdigest()[:4]
    up_open = keys[0] in ALLOWED_CHARS
    down_open = keys[1] in ALLOWED_CHARS
    left_open = keys[2] in ALLOWED_CHARS
    right_open = keys[3] in ALLOWED_CHARS
    return (up_open, down_open, left_open, right_open)

sort_queue = set([(INPUT, (0,0))])
dist: dict[VertexInfo, int] = defaultdict(lambda: float('inf'))
# pt2
dist: dict[VertexInfo, int] = defaultdict(lambda: -float('inf'))
starting_available_dirs = get_allowed_dirs(INPUT)
starting_vertex_info = VertexInfo(INPUT, (0,0), starting_available_dirs)
dist[starting_vertex_info] = 0

def process_new_square(vertex_info: VertexInfo):
    up_open, down_open, left_open, right_open = vertex_info.available_dirs
    cur_loc = vertex_info.coords
    new_path_length = len(vertex_info.path)-N + 1
    # pt2
    new_path_length = -new_path_length
    if up_open and cur_loc[0] > 0:
        new_path = vertex_info.path + "U"
        new_available_dirs = get_allowed_dirs(new_path)
        old_dist = dist[(VertexInfo(new_path, (cur_loc[0]-1,cur_loc[1]), new_available_dirs))]
        if new_path_length < old_dist:
            dist[(VertexInfo(new_path, (cur_loc[0]-1,cur_loc[1]), new_available_dirs))] = new_path_length
    if down_open and cur_loc[0] < H:
        new_path = vertex_info.path + "D"
        new_available_dirs = get_allowed_dirs(new_path)
        old_dist = dist[(VertexInfo(new_path, (cur_loc[0]+1,cur_loc[1]), new_available_dirs))]
        if new_path_length < old_dist:
            dist[(VertexInfo(new_path, (cur_loc[0]+1,cur_loc[1]), new_available_dirs))] = new_path_length
    if left_open and cur_loc[1] > 0:
        new_path = vertex_info.path + "L"
        new_available_dirs = get_allowed_dirs(new_path)
        old_dist = dist[(VertexInfo(new_path, (cur_loc[0],cur_loc[1]-1), new_available_dirs))]
        if new_path_length < old_dist:
            dist[(VertexInfo(new_path, (cur_loc[0],cur_loc[1]-1), new_available_dirs))] = new_path_length
    if right_open and cur_loc[1] < W:
        new_path = vertex_info.path + "R"
        new_available_dirs = get_allowed_dirs(new_path)
        old_dist = dist[(VertexInfo(new_path, (cur_loc[0],cur_loc[1]+1), new_available_dirs))]
        if new_path_length < old_dist:
            dist[(VertexInfo(new_path, (cur_loc[0],cur_loc[1]+1), new_available_dirs))] = new_path_length

while dist:
    print("distances", dist.values())
    min_dist_vertex_info = sorted(dist, key = lambda x: dist[x])[0]
    # pt 2
    # min_dist_vertex_info = sorted(dist, key = lambda x: dist[x])[-1]
    del dist[min_dist_vertex_info]
    if min_dist_vertex_info.coords == TARGET:
        print("BROKE")
        break
    process_new_square(min_dist_vertex_info)
print(min_dist_vertex_info.path)
print(min_dist_vertex_info.path[N:])
print(len(min_dist_vertex_info.path) - N)

        