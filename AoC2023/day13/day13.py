D = open("input13.txt").read()

sections = D.split("\n\n")
print(len(sections))
# print(sections, len(sections))
ans = 0
num_refls = 0
for k, section in enumerate(sections):
    reflection_found = 0
    lines = section.splitlines()
    #Could unpack it to a 1d array and then check for equality back and forth
    W = len(lines[0])
    H = len(lines)
    # unpack_lines = "".join(lines)
    # print(unpack_lines)
    # Check row
    for i in range(1,H):
        width_to_check = min(i, H-i)
        back_slice = lines[i-width_to_check:i]
        forward_slice =lines[i:i+width_to_check]
        forward_slice = list(reversed(forward_slice))
        diffs = sum([sum([1 for a,b in zip(x,y) if a !=b]) for (x,y) in zip(back_slice, forward_slice)])
        # print(i, back_slice, forward_slice)
        if diffs == 1:
                # print("Hori reflect at", i)
                ans += 100*i
                num_refls += 1
                reflection_found += 1
                # break 
    # Check col
    col_lines = [[x[j] for x in lines] for j in range(W)]
    # print(col_lines)
    for j in range(1,W):
        width_to_check = min(j, W-j)
        back_slice = col_lines[j-width_to_check:j]
        forward_slice = col_lines[j:j+width_to_check]
        forward_slice = list(reversed(forward_slice))
        diffs = sum([sum([1 for a,b in zip(x,y) if a !=b]) for (x,y) in zip(back_slice, forward_slice)])
        # print(i, back_slice, forward_slice)
        if diffs == 1:
            # print("Vert reflect at", j)
            ans += j
            num_refls += 1
            reflection_found += 1
            # break
    if reflection_found != 1:
        print(k, reflection_found)
print("Num refls", num_refls)            
print(ans)
    
