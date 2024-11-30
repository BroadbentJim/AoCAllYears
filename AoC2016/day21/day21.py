D = open("input.txt").readlines()
L = [x.strip() for x in D]

INPUT = "abcdefgh"
cur_text = INPUT

def rotate_string(text: str, offset: int, go_right: bool = True) -> str:
    offset %= len(text)
    if go_right:
        return text[-offset:] + text[:-offset]
    else:
        return text[offset:] + text[:offset]
        
# tests = ["abcde", "ebcda", "edcba", "abcde", "bcdea", "bdeac", "abdec", "ecabd", "decab"]
# 
def process_line(cur_text: str, line: str) -> str:
    words = line.split()
    N = len(cur_text)
    # print(line)
    # print(cur_text, test, cur_text == test)
    if words[0] == "swap":
        if words[1] == "position":
            X, Y = [int(x) for x in [words[2], words[-1]]]
            letter_X, letter_Y = cur_text[X], cur_text[Y]
            cur_text = cur_text[:Y] + letter_X + cur_text[Y+1:]
            cur_text = cur_text[:X] + letter_Y + cur_text[X+1:]
        elif words[1] == "letter":
            target_X, target_Y = [words[2], words[-1]]
            new_str = []
            for c in cur_text:
                if c == target_X:
                    new_str.append(target_Y)
                elif c == target_Y:
                    new_str.append(target_X)
                else: new_str.append(c)
            cur_text = "".join(new_str)
    elif words[0] == "rotate":
        if words[1] == "based":
            target_X = words[-1]
            index = cur_text.find(target_X)
            assert index != -1
            offset = index + 1 + int(index>=4)            
            # print("ASDAS", cur_text, offset)
            cur_text = rotate_string(cur_text, offset, go_right=True)
            # print("AS", cur_text)
        elif words[1] in ["left", "right"]:
            offset = int(words[-2])
            cur_text = rotate_string(cur_text, offset, words[1] == "right")
    elif words[0] == "move":
        X, Y = [int(x) for x in [words[2], words[-1]]]
        removed_char = cur_text[X]
        cur_text = cur_text[:X] + cur_text[X+1:]
        cur_text = cur_text[:Y] + removed_char + cur_text[Y:]
    elif words[0] == "reverse":
        X, Y = [int(x) for x in [words[2], words[-1]]]
        middle = "".join(reversed(cur_text[X:Y+1]))
        cur_text = cur_text[:X] + middle + cur_text[Y+1:]
    else:
        raise Exception
    assert len(cur_text) == N, (line, cur_text)
    return cur_text

for line in L:
    cur_text = process_line(cur_text, line)

print(cur_text)
inverse_offset_map = {
   0:1,1:1,2:6, 3:2,4:7,5:3,6:0,7:4
}
def inverse_line(cur_text: str, line: str) -> str:
    words = line.split()
    N = len(cur_text)
    # print(line)
    # print(cur_text, test, cur_text == test)
    if words[0] == "swap":
        if words[1] == "position":
            X, Y = [int(x) for x in [words[2], words[-1]]]
            letter_X, letter_Y = cur_text[X], cur_text[Y]
            cur_text = cur_text[:Y] + letter_X + cur_text[Y+1:]
            cur_text = cur_text[:X] + letter_Y + cur_text[X+1:]
        elif words[1] == "letter":
            target_X, target_Y = [words[2], words[-1]]
            new_str = []
            for c in cur_text:
                if c == target_X:
                    new_str.append(target_Y)
                elif c == target_Y:
                    new_str.append(target_X)
                else: new_str.append(c)
            cur_text = "".join(new_str)
    elif words[0] == "rotate":
        if words[1] == "based":
            target_X = words[-1]
            index = cur_text.find(target_X)
            assert index != -1
            offset = inverse_offset_map[index]
            # print("ASDAS", cur_text, offset)
            cur_text = rotate_string(cur_text, offset, go_right=False)
            # print("AS", cur_text)
        elif words[1] in ["left", "right"]:
            offset = int(words[-2])
            cur_text = rotate_string(cur_text, offset, words[1] == "left")
    elif words[0] == "move":
        X, Y = [int(x) for x in [words[2], words[-1]]]
        Y,X = X,Y
        removed_char = cur_text[X]
        cur_text = cur_text[:X] + cur_text[X+1:]
        cur_text = cur_text[:Y] + removed_char + cur_text[Y:]
    elif words[0] == "reverse":
        X, Y = [int(x) for x in [words[2], words[-1]]]
        middle = "".join(reversed(cur_text[X:Y+1]))
        cur_text = cur_text[:X] + middle + cur_text[Y+1:]
    else:
        raise Exception
    assert len(cur_text) == N, (line, cur_text)
    return cur_text

test = "abcdefgh"
chars = set(test)
line = "rotate based on position of letter "
for char in chars:
    cur_test = test
    cur_line = line + char
    cur_test = process_line(cur_test, cur_line)
    cur_test = inverse_line(cur_test, cur_line)
    assert cur_test == test
    
for line in L:
    cur_test = test
    dedup_test = inverse_line(process_line(cur_test, line), line)
    assert test == dedup_test, (line, dedup_test)
reversed_L = list(reversed(L))
print(reversed_L[:2])
NEW_INPUT = "fbgdceah"
working = NEW_INPUT
for line in reversed_L:
    # print(line)
    working = inverse_line(working, line)
    
print(working)