

with open("input1.txt", "r") as f:
    ans = 0
    for line in f:
        i = 0
        digits = []
        print(line)
        while i < len(line):
            
            char = line[i]
            if char.isdigit():
                digits.append(char)
                i += 1                
                continue
            if i <= len(line)-5:
                if line[i:i+5] == "three":
                    digits.append(3)
                    # i +=5
                    # continue
                elif line[i:i+5] == "seven":
                    digits.append(7)
                    # i +=5
                    # continue
                elif line[i:i+5] == "eight":
                    digits.append(8)
                    # i +=5
                    # continue
                
            if i <= len(line)-4:
                if line[i:i+4] == "four":
                    digits.append(4)
                    # i +=4
                    # continue
                elif line[i:i+4] == "nine":
                    digits.append(9)
                    # i +=4
                    # continue
                elif line[i:i+4] == "five":
                    digits.append(5)
                    # i +=4
                    # continue
            if i <=len(line)-3:
                if line[i:i+3] == "one":
                    digits.append(1)
                    # i +=3
                    # continue
                elif line[i:i+3] == "two":
                    digits.append(2)
                    # i +=3
                    # continue
                elif line[i:i+3] == "six":
                    digits.append(6)
                    # i +=3
                    # continue
            i += 1
        
        print(digits)
        row_num = str(digits[0]) + str(digits[-1])
        print(int(row_num))
        ans += int(row_num)
        
print(ans)
                