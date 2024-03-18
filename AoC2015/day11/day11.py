input = "cqjxjnds"
bad_chars = ['i', 'o', 'l']
def is_valid(password: str) -> str:    
    no_bad_chars = not any([x in password for x in bad_chars])
    has_three_increasing = False
    has_two_pairs = False
    overlap_rights = set()
    for i, first, second, third in zip(range(len(password)), password, password[1:], password[2:]):
        vals = [ord(x) for x in [first, second, third]]
        if vals[1] == vals[0]+1 and vals[2] == vals[1]+1:
            has_three_increasing = True
        if not has_two_pairs and first == second:
            if i in overlap_rights:
                continue
            else:
                if overlap_rights:
                    has_two_pairs = True
                else:
                    overlap_rights.add(i+1)
    if password[-2] == password[-1] and password[-2] != password[-3] and overlap_rights:
        has_two_pairs = True
    # print(no_bad_chars, has_three_increasing, has_two_pairs)
    return no_bad_chars and has_three_increasing and has_two_pairs

def increment_string(password: str) -> str:
    if password[-1] != "z":
        new_char = chr(ord(password[-1])+1)
        return password[:-1] + new_char
    else:
        final_char = "a"
        new_prefix = increment_string(password[:-1])
        return new_prefix + final_char
    
def find_next_valid(password: str) -> str:
    new= password
    while not is_valid(new):
        new = increment_string(new)
    return new
print(is_valid("hijklmn"))
print(is_valid("abbceffg"))
print(is_valid("abbcegjk"))

# print(find_next_valid("abcdefgh"))
# print(find_next_valid("ghijklmn"))
# print(find_next_valid(input))
print(find_next_valid(increment_string("cqjxxyzz")))