import re
# special_chars = ["*", "#", "$", "+", "/", "@", "=", "%", "&"]
nested_list = []
with open("input3.txt", "r") as f:
    for line in f:
        nested_list.append(line.strip())
# print(nested_list)
# ans = 0
# pattern = r"\d+"
# for i, line in enumerate(nested_list):
#     # print(i)
#     print("=" *60)
#     line_len = len(line)
#     matches = re.finditer(pattern,line)
#     for match in matches:
#         print(i, match)
#         start = match.start()
#         end = match.end()
        
#         # print(start, end)
#         if i == 0:
#             container = nested_list[i][max(0,start-1):end+1] + nested_list[i+1][max(0,start-1):end+1]
#         elif i == len(nested_list)-1:
#             container = nested_list[i-1][max(0,start-1):end+1] + nested_list[i][max(0,start-1):end+1]
#         else:
#             container = nested_list[i-1][max(0,start-1):end+1] + nested_list[i][max(0,start-1):end+1] + nested_list[i+1][max(0,start-1):end+1]
#         print(container)
#         part = False
#         # for char in special_chars:
#         #     if char in container:
#         #         part = True
#         for char in container:
#             if not char.isdigit() and char != ".":
#                 part = True
#         if part:
#             print("Part")
#             ans += int(match.group(0))

# print(ans)

ans = 0
gear_locs = {}
for i, line in enumerate(nested_list):
    for j, char in enumerate(line):
        if char == "*":
            print(i,j)
            gear_locs[i,j] = (1,0)

pattern = r"\d+"
for i, line in enumerate(nested_list):
    # print(i)
    print("=" *60)
    line_len = len(line)
    matches = re.finditer(pattern,line)
    for match in matches:
        # print(i, match)
        start = match.start()
        end = match.end()
        
        # print(start, end)
        if i == 0:
            container = nested_list[i][max(0,start-1):end+1] + nested_list[i+1][max(0,start-1):end+1]
        elif i == len(nested_list)-1:
            container = nested_list[i-1][max(0,start-1):end+1] + nested_list[i][max(0,start-1):end+1]
        else:
            container = nested_list[i-1][max(0,start-1):end+1] + nested_list[i][max(0,start-1):end+1] + nested_list[i+1][max(0,start-1):end+1]
        # print(container)
        part = False
        # for char in special_chars:
        #     if char in container:
        #         part = True
        for l, char in enumerate(container):
            if char == "*":
                print(i, match, container, l)
                container_width = 0
                if start >0 and end < line_len:
                    container_width = end-start+2
                else:
                    container_width = end-start+1
                    
                print(container_width)
                n = max(i-1,0) + l // (container_width)
                m = max(start-1,0) + (l % (container_width))
                gear_locs[n,m] = (gear_locs[n,m][0]*int(match.group(0)), gear_locs[n,m][1] +1)

ans = 0
print(gear_locs)
for val, count in gear_locs.values():
    if count >=2 :
        ans += val
print(ans)     