import math
D = open("input.txt").readlines()
L = [x.strip() for x  in D]

ingredients : list[list[int]] = []
for l in L:
    name, vars = l.split(":")
    attrs = vars.split(", ")
    stats = [int(attr.split()[-1]) for attr in attrs]
    ingredients.append(stats)

N = 100
P = len(ingredients) # 4

def generator_simplex(dims: int, total_sum: int):
    if dims == 1:
        yield [total_sum]
        return
    for i in range(total_sum):
        for prefix in generator_simplex(dims-1, total_sum=total_sum-i):
            yield [i] + prefix

def generator_simplex_fixed_calories(dims: int, current_index: int, total_sum: int, fixed_target: int):
    if current_index >= len(ingredients):
        return
    calory_cost = ingredients[current_index][-1]
    if dims == 1 and calory_cost*total_sum == fixed_target:
        yield [total_sum]
        return
    for i in range(total_sum):        
        new_calory_target = fixed_target-i*calory_cost
        for prefix in generator_simplex_fixed_calories(dims-1, current_index+1, total_sum-i, new_calory_target):
            yield [i] + prefix
        

def score_weights(weights: list[int]) -> int:
    assert len(weights) == len(ingredients)
    stat_totals = [sum([ingredient[i] * weight  for ingredient, weight in zip(ingredients, weights)]) for i in range(len(ingredients[0]))]
    stat_totals = [max(x, 0) for x in stat_totals]
    ans = math.prod(stat_totals[:-1])
    return ans

# max_score = 0
# for ingredient_weights in generator_simplex(dims=P, total_sum=N):
#     score = score_weights(ingredient_weights)
#     max_score = max(max_score, score)
# print(max_score)
CALORY_TARGET = 500
max_score = 0
for ingredient_weights in generator_simplex_fixed_calories(dims=P, current_index=0, total_sum=N, fixed_target=CALORY_TARGET):
    score = score_weights(ingredient_weights)
    max_score = max(max_score, score)
print(max_score)