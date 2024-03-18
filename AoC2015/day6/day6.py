D = open("input.txt").readlines()
L = [x.strip() for x in D]

N = 1000
grid = [[0 for _ in range(N)] for _ in range(N)]

def do_toggle(num_1, num_2):
    for x in range(num_1[0], num_2[0]+1):
        for y in range(num_1[1], num_2[1]+1):
            grid[x][y] += 2

def do_turn(value, num_1, num_2):
    for x in range(num_1[0], num_2[0]+1):
        for y in range(num_1[1], num_2[1]+1):
            if value:
                grid[x][y] += 1
            else:
                grid[x][y] = max(grid[x][y]-1, 0)
    
def to_tuple(char: str) -> (int,int):
    x,y = char.split(",")
    return (int(x), int(y))
    

def process_line(line:str):
    words = line.split()
    instruct = words[0]
    assert instruct in ["turn", "toggle"]
    if instruct == "toggle":
        num_1, num_2 = to_tuple(words[1]), to_tuple(words[-1])
        do_toggle(num_1, num_2)
    else:
        dir = words[1]
        assert dir in ["on", "off"]
        value = dir == "on"
        num_1, num_2 = to_tuple(words[2]), to_tuple(words[-1])
        do_turn(value, num_1, num_2)

for l in L:
    print(l)
    process_line(l)

ans = 0
for x in range(N):
    ans += sum(grid[x])
print(ans)
    
    