INPUT = "^^.^..^.....^..^..^^...^^.^....^^^.^.^^....^.^^^...^^^^.^^^^.^..^^^^.^^.^.^.^.^.^^...^^..^^^..^.^^^^"
INPUT = [x == "^" for x in INPUT]
N_ROWS = 400000

GRID = [[False] + INPUT + [False]]

def find_new_entry(a,b,c: bool) -> bool:
    new_entry = False
    if a and b and not c or not a and b and c or a and not b and not c or not a and not b and c:
        new_entry = True
    return new_entry
    


for _ in range(N_ROWS-1):
    cur_row =  GRID[-1]
    interior_row = []
    for a,b,c in zip(cur_row, cur_row[1:], cur_row[2:]):
        new_entry = find_new_entry(a,b,c)
        interior_row.append(new_entry)
    interior_row.insert(0, False)
    interior_row.append(False)
    GRID.append(interior_row)

# for row in GRID:
#     print(row)    
print(sum([x.count(False) -2 for x in GRID]))