input = "1113222113"

def process_string(current: str) -> str:
    new = ""
    i = 1
    current_char = current[0]
    count_length = 1
    while i < len(current):
        new_char = current[i]
        if new_char == current_char:
            count_length += 1            
        else:
            new += str(count_length) + current_char
            current_char = new_char
            count_length = 1
        i += 1
    new += str(count_length) + current_char
    return new

print(process_string("1"))
print(process_string("11"))
print(process_string("21"))
print(process_string("1211"))

new = input
for _ in range(50):
    new = process_string(new)
print(len(new))
