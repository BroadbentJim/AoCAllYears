import re
D = open("input.txt").readlines()
L = [x.strip() for x in D]

W = 50
# W = 7
H = 6
# H = 3
grid = [[0] * W for _ in range(H)]

def process_line(line: str):
    words = line.split(" ")
    instruct = words[0]
    
    if instruct == "rect":
        data = words[1]
        w, h = [int(x) for x in data.split("x")]
        for i in range(h):
            grid[i][:w] = [1] * w
        return
    dir = words[1]
    data = " ".join(words[2:])
    _, data = data.split("=")
    A, B = [int(x) for x in data.split(" by ")]
    if dir == "row":
        grid[A] = grid[A][-B:] + grid[A][:-B]
    elif dir == "column":
        col_data = [row[A] for row in grid]
        shift_col_data = col_data[-B:] + col_data[:-B]
        for i in range(H):
            grid[i][A] = shift_col_data[i]

for l in L:
    process_line(l)
for row in grid:
    text = list(map(lambda x: "#" if x else ".", row))
    print("".join(text))
ans = sum([sum(row) for row in grid])
print(ans)