from dataclasses import dataclass
D = open("input.txt").readlines()
L = [x.strip() for x in D]

L = L[2:]

@dataclass
class Node:
    node_coords: tuple[int,int]
    size: int
    used: int
    avail: int

def process_line(line:str) -> Node:
    filename, *numeric = line.split()
    _, _,_, node_name = filename.split("/")
    node_name = node_name[5:]
    x,y = [int(x[1:]) for x in node_name.split("-")]
    size, used, avail, _ = [int(x[:-1]) for x in numeric]
    node = Node((x,y), size, used, avail)
    return node

nodes: list[Node] = []
for line in L:
    node = process_line(line)
    nodes.append(node)
ans = 0
for A_node in nodes:
    if A_node.used == 0:
        empty_loc = A_node.node_coords
        continue
    for B_node in nodes:        
        if A_node.node_coords != B_node.node_coords and A_node.used <= B_node.avail:
            ans += 1
print(ans)
node_grid = []
W,H = [x+1 for x in nodes[-1].node_coords]
print(W,H, W*H, len(nodes))
for i in range(0, W*H, H):
    node_slice = nodes[i:i+H]
    node_grid.append(node_slice)
node_grid = [[x[i] for x in node_grid] for i in range(H)]
assert len(node_grid) == H
assert all([len(row) == W for row in node_grid])
assert node_grid[-1][-1] == nodes[-1]


def node_to_character(node: Node) -> str:
    if node.used == 0:
        return "_"
    elif node.node_coords == (W-1, 0):
        return "G"
    elif node.node_coords == (0,0):
        return "S"
    elif node.size > 300:
        return "#"
    elif node.size < 120:
        return "."
    else:
        print(node)

for row in node_grid:
    row_str = [node_to_character(node) for node in row]
    print("".join(row_str))
    
cost_to_move_G_left_one = 5
    
ans = 6+empty_loc[1]+7 #TO next to G
# ans = 1
ans += 5*(W-2) #To move G next to S
ans += 1 #To move onto S
print(ans)