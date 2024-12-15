D= open("input.txt").readlines()

G = [list(x.strip()) for x in D]
# G = [int(x) for x in D]
G = [['.'] + x + ['.'] for x in G]
G = [['.'] * len(G[0])] + G + [['.'] * len(G[0])]
print(G)
H,W = len(G),len(G[0])
trail_heads = []

for i, row in enumerate(G):
    for j, char in enumerate(row):
        if char == '0':
            trail_heads.append((i,j))
print(trail_heads)
print(len(trail_heads))

adjs = [(-1,0), (1,0),(0,1),(0,-1)]

def do_walk(nines_seen, cur_pos, target) -> int:
    score = 0
    for neighbour in [(cur_pos[0]+dir[0], cur_pos[1]+dir[1]) for dir in adjs]:
        if G[neighbour[0]][neighbour[1]] == str(target):
            if target == 9:
                nines_seen.add(neighbour)
            else:
                score += do_walk(nines_seen, neighbour, target + 1)
    return score
        
            


ans = 0            
for trail_head in trail_heads:
    cur_pos = trail_head
    nines_seen = set()
    do_walk(nines_seen, cur_pos, target=1)    
    ans += len(nines_seen)
print(ans)



def do_walk_2(cur_pos, target) -> int:
    score = 0
    for neighbour in [(cur_pos[0]+dir[0], cur_pos[1]+dir[1]) for dir in adjs]:
        if G[neighbour[0]][neighbour[1]] == str(target):
            if target == 9:
                score += 1
            else:
                score += do_walk_2(neighbour, target + 1)
    return score
        
            


ans = 0            
for trail_head in trail_heads:
    cur_pos = trail_head
    score = do_walk_2(cur_pos, target=1)    
    ans += score
print(ans)