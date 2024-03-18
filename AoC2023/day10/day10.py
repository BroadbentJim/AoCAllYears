from itertools import product
D = open("input10.txt").read().strip()
L = D.splitlines()
W = len(L[0])
# H = len(L)

L = ["." + x + "." for x in L]
L.insert(0, "." * (W+2))
L.append("." * (W+2))

def go_next(i,j,direction, char):
    # Direction is the incident direction
    NS = ["N", "S"]
    EW = ["E", "W"]
    if direction in NS:
        if direction == NS[0]:
            direction = NS[1]
        else:
            direction = NS[0]
    else:
        if direction == EW[0]:
            direction = EW[1]
        else:
            direction = EW[0]
    
    match char:
        case "|":
            if direction not in ["N", "S"]:
                return False
            else:
                if direction == "N":
                    return i,j+1, "S"
                else:
                    return i,j-1, "N"
        case "-":
            if direction not in ["E", "W"]:
                return False
            else:
                if direction == "E":
                    return i-1,j, "W"
                else:
                    return i+1,j, "E"
        case "L":
            if direction not in ["N", "E"]:
                return False
            else:
                if direction == "N":
                    return i+1,j, "E"
                else:
                    return i,j+1, "N"
        case "J":
            if direction not in ["N", "W"]:
                return False
            else:
                if direction == "N":
                    return i-1,j, "W"
                else:
                    return i,j-1, "N"
        case "7":
            if direction not in ["S", "W"]:
                return False
            else:
                if direction == "W":
                    return i,j-1, "S"
                else:
                    return i-1,j, "W"
        case "F":
            if direction not in ["S", "E"]:
                return False
            else:
                if direction == "E":
                    return i,j-1, "S"
                else:
                    return i+1,j, "S"
        case ".":
            return False
        case "S":
            return i,j,direction

def look_for_loop(start, start_dir):
    print(start, start_dir)
    loop_length = 0
    cur_pos = start
    cur_dir = start_dir
    cur_tile = L[start[0]][start[1]]
    while cur_tile != "S":
        print(cur_pos, cur_dir, cur_tile)
        result = go_next(*cur_pos, cur_dir, cur_tile)
        if not result:
            return False
        if len(result) == 1:
            break
        print(result)
        new_posl, new_posr, new_dir = result
        new_pos = (new_posl, new_posr)
        # print(new_pos, new_dir)
        loop_length += 1
        cur_pos = new_pos
        cur_dir = new_dir
        cur_tile = L[cur_pos[0]][cur_pos[1]]
    
    return loop_length
        
ans = 0
for i, line in enumerate(L):
    for j, char in enumerate(line):
        if char == "S":
            print(i,j)
            print("North")
            a = look_for_loop((i-1,j), "N")
            print("South")
            b = look_for_loop((i+1,j), "S")
            print("West")
            c = look_for_loop((i,j-1), "W")
            print("East")
            d = look_for_loop((i,j+1), "E")
            # print(a,b,c,d)
            # print(a+b+c+d)
            # ans = a+b+c+d
            ans = a+c
            break
            
print(ans)