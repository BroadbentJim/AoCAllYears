input = "^v"
san_x_coord = 0
san_y_coord = 0
rob_x_coord = 0
rob_y_coord = 0
locs_visited ={(0,0)}
for i, char in enumerate(input):
    if i % 2:
        x_coord, y_coord = rob_x_coord, rob_y_coord
    else:
        x_coord, y_coord = san_x_coord, san_y_coord
    match char:
        case ">":
            x_coord +=1
        case "^":
            y_coord += 1
        case "<":
            x_coord -= 1
        case "v":
            y_coord -= 1
    locs_visited.add((x_coord,y_coord))
    
    if i % 2:
        rob_x_coord, rob_y_coord = x_coord, y_coord
    else:
        san_x_coord, san_y_coord = x_coord, y_coord
print(len(locs_visited))