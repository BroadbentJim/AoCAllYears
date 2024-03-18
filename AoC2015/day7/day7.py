# 16 bit logic gates
from dataclasses import dataclass
from functools import cache
"""
Methodology:
Can read in all mentioned wire names
and build a graph. The image I have in my head is the wires go left to right with other branches bringing info into other branches
Slight concern around whether we are using SSA
i.e. do branches get set to multiple times
"""
D = open("input.txt").readlines()
L = [l.strip() for l in D]

@dataclass
class Instruction:
    operation: str
    children: (int) | (str) | (str | str)

children: dict[str, Instruction]= {}
for l in L:
    source, target = l.split(" -> ")
    list_source = source.split()    
    if len(list_source) == 2:
        child = Instruction(list_source[0], (list_source[1],))
    elif len(list_source) == 3:        
        child = Instruction(list_source[1], (list_source[0], list_source[2]))
    elif len(list_source) == 1:
        if source.isnumeric():
            child = Instruction("ORIGIN", (int(list_source[0]),))
        else:
            child = Instruction("PASSTHROUGH", (list_source[0],))
    else:
        print(list_source)
        print("BAD")
    if target in children:
        print("Var set too twice")        
    children[target] = child
# memo = set()
# visited = []
@cache
def find_recursive(root: str) -> int:
    # visited.append(root)
    # if root in memo:
    #     print(visited)
    #     raise ValueError    
    # memo.add(root)
    if root.isnumeric():
        return int(root)
    child = children[root]
    match child.operation:
        case "ORIGIN":
            return child.children[0]
        case "PASSTHROUGH":
            return find_recursive(child.children[0])
        case "NOT":
            return 65535 - find_recursive(child.children[0])
        case "AND":
            a = find_recursive(child.children[0])
            b = find_recursive(child.children[1])
            return a & b
        case "OR":
            a = find_recursive(child.children[0])
            b = find_recursive(child.children[1])
            return a | b
        case "LSHIFT":
            a = find_recursive(child.children[0])
            n = int(child.children[1])
            return a << n
        case "RSHIFT":
            a = find_recursive(child.children[0])
            n = int(child.children[1])
            return a >> n
        case _:
            print(root, child)
            raise ValueError
        
# answers = {x: find_recursive(x) for x in children.keys()}
# print(answers)
        
ans = find_recursive("a")
print(ans)
children["b"] = Instruction("ORIGIN", children=(int(ans),))
find_recursive.cache_clear()
print(find_recursive("a"))
