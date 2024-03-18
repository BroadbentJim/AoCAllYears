from dataclasses import dataclass
D = open("input.txt").readlines()
L = [x.strip() for x in D]

@dataclass
class ReindeerStat:
    vel: int
    travel_time: int
    rest_time: int
reindeer_stats : dict[str, ReindeerStat] = {}

for l in L:
    words = l.split()
    name, vel, time, rest_period = words[0], words[3], words[6], words[-2]
    reindeer_stats[name] = ReindeerStat(int(vel), int(time), int(rest_period))
print(reindeer_stats)

def simulate_reindeer(reindeer_stat: ReindeerStat, time_period: int) -> int:
    go_rest_time = reindeer_stat.travel_time + reindeer_stat.rest_time
    travel_periods = time_period // go_rest_time
    bonus = time_period % go_rest_time
    ans = travel_periods * reindeer_stat.travel_time * reindeer_stat.vel + min(bonus,reindeer_stat.travel_time) * reindeer_stat.vel
    return ans

T = 2503
# travel_distances = {x: simulate_reindeer(stat, T) for (x,stat) in reindeer_stats.items()}
# print(travel_distances)
# max_dist = 0
# for (name, dist) in travel_distances.items():
#     if dist > max_dist:
#         winner = name
#         max_dist = dist
        
# print(winner, max_dist)

def simulate_reindeer_explicit(reindeer_stat: ReindeerStat, time_period: int) -> list[int]:
    ans = []
    current = 0
    go_rest_time = reindeer_stat.travel_time + reindeer_stat.rest_time
    travel_periods = time_period // go_rest_time
    bonus = time_period % go_rest_time
    for _ in range(travel_periods):
        new = [current + reindeer_stat.vel * i for i in range(1,reindeer_stat.travel_time+1)]
        final = new[-1]
        new += [final] * reindeer_stat.rest_time
        current = final
        ans += new
    ans += [current + reindeer_stat.vel * (i+1) for i in range(0, min(bonus, reindeer_stat.travel_time))]
    # print(reindeer_stat, ans)
    final = ans[-1]
    ans += [final] * (bonus-reindeer_stat.travel_time)
    return ans

travel_distances = {x: simulate_reindeer_explicit(stat, T) for (x,stat) in reindeer_stats.items()}
print([len(x) for x in travel_distances.values()])
scores = {x: 0 for x in travel_distances.keys()}
for i in range(T):
    # print(i)
    current_distances = {name: travel_distances[name][i] for name in scores}
    max_dist = max(current_distances.values())
    current_winners: set[str] = {deer for deer, dist in current_distances.items() if dist == max_dist}
    for winner in current_winners:
        scores[winner] += 1
print(scores)
print(max(scores))
    
