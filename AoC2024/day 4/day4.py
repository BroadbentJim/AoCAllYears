D = open("input.txt").read().splitlines()
print(D)
D = ['#'*6 + x.strip() + '#'*6 for x in D]
D = ['#' * len(D[0])]*8 + D + ['#' * len(D[0])]*8
print(D)

# Main concern don't double count the same word twice
# First check and then we can check double counting
# print(len(D[0]), len(D))
ans = 0
for i, row in enumerate(D):
    for j, char in enumerate(row):
        if char == 'X':
            # print(i,j)
            for dir in [(1,0), (1,1), (0,1), (1,-1), (-1,0), (-1,-1), (0,-1), (-1,1)]:
                if D[i+dir[0]][j+dir[1]] == 'M':
                    if D[i+2*dir[0]][j+2*dir[1]] == 'A':
                        # print(i+3*dir[0],j+3*dir[1])
                        if D[i+3*dir[0]][j+3*dir[1]] == 'S':
                            ans += 1
print(ans)                        

ans = 0
for i, row in enumerate(D):
    for j, char in enumerate(row):
        if char == 'A':
            if set((D[i-1][j-1],D[i+1][j+1])) == {'S', 'M'} and set((D[i+1][j-1],D[i-1][j+1])) == {'S', 'M'}:
                ans += 1
print(ans)                
            