D = open("input.txt").readlines()
L = [x.strip() for x in D]

# def is_nice(word: str):
#     vowels = ["a", "e", "i", "o", "u"]
#     vowel_count = sum([word.count(x) for x in vowels])
#     pair = False
#     not_allowed_strs = ["ab", "cd", "pq", "xy"]
#     not_allowed = False
#     for char, char_2 in zip(word, word[1:]):
        
#         pair = pair or (char == char_2)
#         not_allowed = not_allowed or (char+char_2) in not_allowed_strs
    
#     nice = vowel_count >=3 and pair and (not not_allowed)
#     return nice

def is_nice(word: str):
    is_repeat = False
    seen_pair = False
    seen_char_pairs = {}
    left_coord = 0
    for char, char_1, char_2 in zip(word, word[1:], word[2:]):
        is_repeat |= char == char_2
        if (char, char_1) in seen_char_pairs:
            left_coord_prev = seen_char_pairs[(char, char_1)]
            seen_pair |= (left_coord_prev < left_coord-1)
        if (char, char_1) not in seen_char_pairs:
            seen_char_pairs[(char, char_1)] = left_coord
        left_coord += 1
    if (word[-2], word[-1]) in seen_char_pairs:
        right_coord_prev = seen_char_pairs[(word[-2], word[-1])]
        seen_pair |= right_coord_prev < left_coord-1
    return is_repeat and seen_pair

answers = [is_nice(l) for l in L]

print(sum(answers))             
