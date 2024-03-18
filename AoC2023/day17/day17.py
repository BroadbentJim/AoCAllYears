from queue import PriorityQueue
D = open("input17.txt").read().splitlines()

max_val = 0
for line in D:
    for val in line:
        max_val = max(max_val, int(val))


D = [[float('inf')] + [int(a) for a in x] + [float('inf')] for x in D]

W = len(D[0])
D = [[float('inf')]* W]  + D + [[float('inf')]* W] 
# print(D)



W = len(D[0])
H = len(D)
dists = {}
prevs = {}
dists[(1,1)] = (0, ("U", 0))
queue = PriorityQueue()



for i,line in enumerate(D):
    for j, char in enumerate(line):
        if i in [0,H-1] or j in [0,W-1]:
            dists[(i,j)] = (float('inf'), ("U", 0))
            continue
        if (i,j) != (1,1):
            dists[(i,j)] = (float('inf'), ("U", 0)) # Distance from top left, direction travelled from num squares.
            prevs[(i,j)] = []
        queue.put((dists[(i,j)][0], (i,j)))
        # line[j] = int(char)

# def find_min_dist(dists, queue):
    
#     cur_min = float('inf')
#     coord_min = (0,0)
#     for coord, dist in dists.items():
#         if coord not in queue:
#             continue
#         # print(coord, dist, cur_min, dist[0])
#         if dist[0] < cur_min:
#             coord_min = coord
#             cur_min = dist[0]
#     return coord_min        
    
print(dists)
while not queue.empty():
    # print(queue)
    dist_u = queue.get()
    u = dist_u[1]
    i,j = u
    cur_dist, trajectory = dists[u]
    for direction, (x,y) in zip(['U','R','L','D'], [[1,0], [0,1], [-1,0], [0,-1]]):
        l,k = i+x,j+y
        old_dist = dists[(l,k)][0]
        new_dist = cur_dist + D[l][k]
        if new_dist < old_dist and (direction != trajectory[0] or trajectory[1] < 3):
            if direction == trajectory[1]:
                dists[(l,k)] = (new_dist, (direction, trajectory[1]+1))
            else:
                dists[(l,k)] = (new_dist, (direction, 1))
                
print(dists)
                
        
        
    
