from hashlib import md5
from collections import defaultdict
from dataclasses import dataclass
INPUT = "ihgpwlah"
TARGET = (3,3)
ALLOWED_CHARS = ["b", "c", "d", "e", "f"]
N = len(INPUT)

W = 3
H = 3

@dataclass(frozen=True)
class CoordInfo:
    coords: tuple[int,int]
    available_dirs: tuple[bool,bool,bool,bool]

@dataclass(frozen=True)
class PathData:
    path: str
    coord_info: CoordInfo

def get_allowed_dirs(path: str) -> tuple[bool,bool,bool,bool]:
    keys = md5(path.encode()).hexdigest()[:4]
    up_open = keys[0] in ALLOWED_CHARS
    down_open = keys[1] in ALLOWED_CHARS
    left_open = keys[2] in ALLOWED_CHARS
    right_open = keys[3] in ALLOWED_CHARS
    return (up_open, down_open, left_open, right_open)

dist: dict[CoordInfo, int] = defaultdict(int)

starting_available_dirs = get_allowed_dirs(INPUT)
starting_coord_info = CoordInfo((0,0), starting_available_dirs)
dist[starting_coord_info] = 0
cur_longest_path: dict[CoordInfo, str] = {starting_coord_info: INPUT}

def process_new_square(path_data: PathData):
    vertex_info = path_data.coord_info
    up_open, down_open, left_open, right_open = vertex_info.available_dirs
    cur_loc = vertex_info.coords
    new_path_length = len(path_data.path)-N + 1
    if up_open and cur_loc[0] > 0:
        new_path = path_data.path + "U"
        new_available_dirs = get_allowed_dirs(new_path)
        new_coord_info = CoordInfo((cur_loc[0]-1,cur_loc[1]), new_available_dirs)
        old_dist = dist[new_coord_info]
        if new_path_length > old_dist:
            dist[new_coord_info] = new_path_length
            cur_longest_path[new_coord_info] = new_path
    if down_open and cur_loc[0] < H:
        new_path = path_data.path + "D"
        new_available_dirs = get_allowed_dirs(new_path)
        new_coord_info =(CoordInfo((cur_loc[0]+1,cur_loc[1]), new_available_dirs)) 
        old_dist = dist[new_coord_info]
        if new_path_length > old_dist:
            dist[new_coord_info] = new_path_length
            cur_longest_path[new_coord_info] = new_path
    if left_open and cur_loc[1] > 0:
        new_path = path_data.path + "L"
        new_available_dirs = get_allowed_dirs(new_path)
        new_coord_info =(CoordInfo((cur_loc[0],cur_loc[1]-1), new_available_dirs))
        old_dist = dist[new_coord_info]
        if new_path_length > old_dist:
            dist[new_coord_info] = new_path_length
            cur_longest_path[new_coord_info] = new_path
    if right_open and cur_loc[1] < W:
        new_path = path_data.path + "R"
        new_available_dirs = get_allowed_dirs(new_path)
        new_coord_info = (CoordInfo((cur_loc[0],cur_loc[1]+1), new_available_dirs))
        old_dist = dist[new_coord_info]
        if new_path_length > old_dist:
            dist[new_coord_info] = new_path_length
            cur_longest_path[new_coord_info] = new_path
            
while dist:
    # print(len(dist))
    # print(cur_longest_path)
    min_dist_vertex_info = sorted(dist, key = lambda x: dist[x])[-1]
    del dist[min_dist_vertex_info]
    path = cur_longest_path[min_dist_vertex_info]
    path_data = PathData(path, min_dist_vertex_info)
    if min_dist_vertex_info.coords == TARGET:
        print(len(path)-N)
    process_new_square(path_data)
print(path)
print(len(path)-N)
