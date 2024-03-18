D = open("input.txt").readlines()
L = [x.strip() for x in D]

grid = [[x for x in range(i,i+3)] for i in range(1,9,3)]
print(grid)
def process_line(start_pos, line):
    current_pos = start_pos
    for move in line:
        match move:
            case "U":
                current_pos[0] = max(0, current_pos[0]-1)
                
            case "L":
                current_pos[1] = max(0, current_pos[1]-1)
            case "D":
                current_pos[0] = min(2, current_pos[0]+1)
            case "R":
                current_pos[1] = min(2, current_pos[1]+1)
                
        # print(current_pos)
    return current_pos

current_pos = [1,1]
ans = []
for line in L:
    print("LINE", line)
    current_pos = process_line(current_pos, line)
    ans.append(grid[current_pos[0]][current_pos[1]])
print(ans)

grid = [[0]*(2-i) + [x for x in range(i**2 +1,(i+1)**2+1)] + [0]*(2-i) for i in range(3)]
grid += [["0", "A", "B", "C", "0",]]
grid += [["0"] * 2 + ["D"] + ["0"] * 2]
assert all([len(x) == 5 for x in grid])
print(grid)

def process_line2(start_pos, line):
    current_pos = start_pos
    for move in line:
        match move:
            case "U":
                if current_pos[1] < 2:
                    current_pos[0] = max(2-current_pos[1], current_pos[0]-1)
                else:
                    current_pos[0] = max(current_pos[1]-2, current_pos[0]-1)
            case "L":
                current_pos[1] = max(abs(2-current_pos[0]), current_pos[1]-1)
            case "D":
                current_pos[0] = min(4-abs(2-current_pos[1]), current_pos[0]+1)
            case "R":
                current_pos[1] = min(4-abs(2-current_pos[0]), current_pos[1]+1)
        print(current_pos)
    return current_pos

current_pos=[2,0]
ans = []
for line in L:
    print(f"{line=}")
    current_pos = process_line2(current_pos, line)
    ans.append(grid[current_pos[0]][current_pos[1]])
    
print(ans)