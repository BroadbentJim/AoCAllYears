D = open("input.txt").readlines()
L = [x.strip() for x in D]
def process_string(line: str) -> (int, int):
    char_codes = len(line)
    char_memory = 0
    i = 0
    while i < len(line):
        char = line[i]
        if char != "\\":
            char_memory += 1
            i += 1
        else:
            if line[i+1] in ['\\', '\"']:
                char_memory += 1
                i += 2
            elif line[i+1] == "x":
                char_memory += 1
                i += 4
            else:
                print("BAD")
    char_memory = char_memory -2 #Exclude first and last "
    return char_codes, char_memory


def process_string2(line: str) -> (int, int):
    char_codes = len(line)
    char_encoded = 6 #Takes 6 chars to represent ""
    line_trimmed = line[1:-1]
    for char in line_trimmed:
        if char == '\\':
            char_encoded += 2
        elif char == '\"':
            char_encoded += 2
        else:
            char_encoded += 1                       
    
    return char_codes, char_encoded

all_codes = 0
all_memory = 0
for line in L:
    line_code, line_memory = process_string(line)
    all_codes += line_code
    all_memory += line_memory
print(all_codes, all_memory)
print(all_codes-all_memory)

all_codes = 0
all_encoded = 0
for line in L:
    line_code, line_encoded = process_string2(line)
    all_codes += line_code
    all_encoded += line_encoded
print(all_encoded, all_codes)
print(all_encoded-all_codes)