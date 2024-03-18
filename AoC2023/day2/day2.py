# red_max = 12
# green_max = 13
# blue_max = 14 
with open("input2.txt", 'r') as f:
    ans = 0
    for i, line in enumerate(f):
        # print(line)
        gameID = i+1
        valid = True
        iter_ = iter(line)
        char = next(iter_)
        while char != ":":
            char = next(iter_)
        goes = "".join(list(iter_)).split(";")
        # print(goes)
        red_max = 0
        blue_max = 0
        green_max = 0
        for go in goes:
            go_s = go.split(", ")
            # print(go_s)
            for term in go_s:
                term_count = int("".join([x for x in term if x.isdigit()]))
                if "red" in term:
                    red_max = max(red_max, term_count)
                elif "blue" in term:
                    blue_max = max(blue_max, term_count)
                elif "green" in term:
                    green_max = max(green_max, term_count)
        power_cubes = red_max*green_max*blue_max
        ans += (power_cubes)
        
print(ans)
                 
                    
        
        