from dataclasses import dataclass

@dataclass(frozen=False)
class Robot:
    p_x: int
    p_y: int
    v_x: int
    v_y: int

D = open("input.txt").readlines()

H,W = 103,101

robots: list[tuple[tuple[int,int], tuple[int,int]]] = []
for line in D:
    line = line.strip()
    ps,vs = line.split(" ")
    ps = ps.split("=")[1]
    ps = ps.split(",")
    p_x, p_y = int(ps[0]), int(ps[1])
    vs = vs.split("=")[1]
    vs = vs.split(",")
    v_x, v_y = int(vs[0]), int(vs[1])
    robots.append(((p_x,p_y), (v_x,v_y)))
print("R", len(robots))


def transform(robots, T):
    transformed_robots = []
    for robot in robots:
        p,v = robot
        delta_v = (v[1]*T % H, v[0] * T %W)
        final_p = ((p[1]+delta_v[0]) % H, (p[0]+delta_v[1]) % W)
        transformed_robots.append(final_p)
    return transformed_robots


# PT:1
# T = 100
# transformed_robots = transform(robots, T)
# print(transformed_robots)
# quadrants = [[0,0], [0,0]]
# for robot_pos in transformed_robots:
#     if robot_pos[0] < H // 2:
#         i = 0
#     elif robot_pos[0] > H // 2:
#         i = 1    
#     else:
#         print(robot_pos)
#         continue
#     if robot_pos[1] < W // 2:
#         j = 0
#     elif robot_pos[1] > W // 2:
#         j = 1
#     else:
#         print(robot_pos)
#         continue    
#     quadrants[i][j] += 1
# print(quadrants)
# ans = 1
# for r in quadrants:
#     for j in r:
#         ans *= j
# print(ans)


from itertools import product

all_dirs = product([-1,0,1], repeat=2)


def calculate_connected_component(robots: list[Robot]) -> int:
    robot_positions = [(robot.p_y, robot.p_x) for robot in robots]
    set_robots = set(robot_positions)
    global_has_visited = set()
    ans = 0
    for i in range(3):
        cands = [pos for pos in robot_positions if pos not in set_robots]
        if not cands:
            break        
        items = [cands[0]]
        local_has_visited = set()
        while items:
            robot = items.pop()
            global_has_visited.add(robot)
            local_has_visited.add(robot)
            for dir in all_dirs:
                new_loc = (robot[0]+dir[0], robot[1]+dir[1])
                if new_loc in set_robots and new_loc not in global_has_visited and new_loc not in global_has_visited:
                    items.append(new_loc)
        ans = max(ans, len(local_has_visited))
    return ans

N = len(robots)


def propagate(robots: list[Robot]) -> list[Robot]:
    # Move on for 1 timestep
    for robot in robots:
        final_p = ((robot.p_y+robot.v_y) % H, (robot.p_x+robot.v_x) % W)
        robot.p_x = final_p[1]
        robot.p_y = final_p[0]
    return robots


i = 0


dataclass_robots = [Robot(p_x=x[0][1], p_y=x[0][0], v_x=x[1][1], v_y=x[1][0]) for x in robots]
working_robots = dataclass_robots
while True:
    working_robots = propagate(working_robots)
    comp_size = calculate_connected_component(working_robots)
    # print(working_robots[:3])
    # print(i, comp_size, comp_size / N)
    if i % 1000 == 0:
        print(i, comp_size)
    if comp_size / N > 0.1:
        print("HJERAS", i)
        break
    i += 1