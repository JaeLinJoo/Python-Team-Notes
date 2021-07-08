#치킨배달 (완전탐색)
from itertools import combinations

n,m = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(n)]

def distance(p1,p2):
    dist = abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
    return dist

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i,j))

min_sum = int(1e9)
comb_ch = combinations(chicken, m)
for comb in comb_ch:
    res = 0
    for h in house:
        res += min(distance(h, c) for c in comb)
    if res <= min_sum:
        min_sum = res

print(min_sum)