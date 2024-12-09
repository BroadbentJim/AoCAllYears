D= open("input.txt").readlines()

L = [int(x) for x in D[0].strip()]

# Construct sparse repr

mem_repr = []
for ix, char in enumerate(L):
    is_block = ix % 2 == 0
    if is_block:
        id = ix // 2
        mem_repr += [id]*char
    else:
        mem_repr += ['.']*char

# print(mem_repr)

left_most_free_spot = 0
while mem_repr[left_most_free_spot] != '.':
    left_most_free_spot += 1
    
right_most_full_spot = len(mem_repr)-1
while mem_repr[right_most_full_spot] == '.':
    right_most_full_spot -= 1
    
while left_most_free_spot < right_most_full_spot:
    # print(left_most_free_spot, right_most_full_spot)
    val = mem_repr.pop(right_most_full_spot)
    right_most_full_spot -= 1    
    mem_repr[left_most_free_spot] = val
    while left_most_free_spot < len(mem_repr) and mem_repr[left_most_free_spot] != '.':
        left_most_free_spot += 1
    while right_most_full_spot >= 0 and mem_repr[right_most_full_spot] == '.':
        right_most_full_spot -= 1

ans = sum([i*int(x) if x != '.' else 0 for i,x in enumerate(mem_repr)])
print(ans)


L = [int(x) for x in D[0].strip()]
# second coordinate == True <-> Describes a file not empty space
L_marked = [(x, i%2 == 0, i // 2 if i % 2 == 0 else -1) for i,x in enumerate(L)]
print(L_marked)
right_attempt = len(L) -1
while right_attempt > 0:
    block_size, is_block, block_id = L_marked[right_attempt]
    if not is_block:
        right_attempt -= 1
        continue    
    leftmost_gap = 1
    # print(block_size, is_block, block_id)
    # print(L_marked[leftmost_gap])
    while leftmost_gap < right_attempt:
        block = L_marked[leftmost_gap]
        if block[1] is False and block[0] >= block_size:
            break
        leftmost_gap += 1
    if leftmost_gap < right_attempt:
        # What happens here
        # First check that we have the right target
        prev_empty_block = L_marked[leftmost_gap]
        assert prev_empty_block[1] is False
        assert prev_empty_block[0] >= block_size
        assert prev_empty_block[2] == -1
        new_block = prev_empty_block[0] -block_size, prev_empty_block[1], prev_empty_block[2]
        # print(1, L_marked)
        # Then we can zero at the end
        L_marked[right_attempt] = (block_size, False, -1)
        # print(2, L_marked)
        # Then we want to insert this ahead of the target
        # Then we want to amend the target
        # We can either modify in place and remove if empty
        # Or we can pop, modify and assert
        # Let's modify in place 
        # print(3,L_marked)
        if new_block[0] == 0:
            L_marked.pop(leftmost_gap)
        else:
            L_marked[leftmost_gap] = new_block
        # print(4,L_marked)
        L_marked.insert(leftmost_gap, (block_size, is_block, block_id))
        
    right_attempt -= 1

print(L_marked)

mem_repr =[]
for val in L_marked:
    if val[1] is False:
        mem_repr += ['.']*val[0]
    else:
        mem_repr += [val[2]]*val[0]
print(mem_repr)

ans = sum([i*int(x) if x != '.' else 0 for i,x in enumerate(mem_repr)])
print(ans)