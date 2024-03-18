D = open("input15.txt").read().strip()

parts = D.split(",")

def hash_algo(part):
    cur = 0
    for char in part:
        cur += ord(char)
        cur *= 17
        cur %= 256
    return cur

def process_part(part):
    if "=" in part:
        key, val = part.split("=")
        # print(sloc)
        hash = hash_algo(key)
        dataset = hashmap[hash]
        for i, holder in enumerate(dataset):
            # print(holder)
            (target_sloc, _) = holder
            if target_sloc == key:
                dataset[i] = (key, val)
                return
        dataset.append((key, val))
    elif "-" in part:
        key, _ = part.split("-")
        hash = hash_algo(key)
        dataset = hashmap[hash]
        i = 0
        while i < len(dataset):
            target_sloc, _ = dataset[i]
            if target_sloc == key:
                del dataset[i]
                return
            i += 1
hashmap = [[] for _ in range(256)]

for part in parts:
    process_part(part)
    # print(part)
    # print(hashmap[:5])


ans = 0
for box_n, box in enumerate(hashmap):
    for i, (_,lens) in enumerate(box):
        # print(lens)
        lens = int(lens)
        cur_val = (1+box_n) * (i+1) * lens
        ans += cur_val
print(ans)