from dataclasses import dataclass
D = open("input.txt").readlines()
L = [l.strip() for l in D]

@dataclass
class SueData:
    children: int = None
    cats: int = None
    samoyeds: int = None
    pomeranians: int = None
    akitas: int = None
    vizslas: int = None
    goldfish: int = None
    trees: int = None
    cars: int = None
    perfumes: int = None
sue_datas : list[SueData] = []
for l in L:    
    words = l.split(":")
    words = words[1:]
    words = " ".join(words)
    results = words.split(", ")
    # print(results)
    records = {}
    for result in results:
        attr, val = result.split()
        records[attr] = int(val)
    local_sue_data = SueData(**records)
    sue_datas.append(local_sue_data)
given_data = SueData(
    children = 3,
    cats = 7,
    samoyeds = 2,
    pomeranians = 3,
    akitas = 0,
    vizslas = 0,
    goldfish = 5,
    trees = 3,
    cars = 2,
    perfumes = 1,
)
field_names = list(given_data.__dict__.keys())
num_attrs = len(field_names)
min_diff = num_attrs
target = -1

def count_differing_attributes(obj1, obj2):
    diff_count = 0
    for field_name in field_names:
        val1 = getattr(obj1, field_name)
        val2 = getattr(obj2, field_name)
        diff_count += val1 != val2
    return diff_count

def count_differing_attributes_pt2(obj1, obj2):
    diff_count = 0
    for field_name in field_names:
        val1 = getattr(obj1, field_name)
        val2 = getattr(obj2, field_name)
        if field_name in ["cats", "trees"]:
            diff_count += val1 is None or val1 <= val2
        elif field_name in ["pomeranians", "goldfish"]:
            diff_count += val1 is None or val1 >= val2
        else:
            diff_count += val1 != val2
    return diff_count


for i, sue_data in enumerate(sue_datas):
    diff_count = count_differing_attributes_pt2(sue_data, given_data)
    print(diff_count)
    if diff_count < min_diff:
        target = i+1
        min_diff = diff_count
print(min_diff)
print(target)