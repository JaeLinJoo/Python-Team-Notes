#치킨치킨치킨
from itertools import combinations

n, m = map(int,input().split())

a = []
for i in range(n):
  a.append(list(map(int,input().split())))

chicken = [0+i for i in range(m)]
comb = list(combinations(chicken,3))

max_sum = 0
for c in comb:
  s_sum = 0
  for i in range(n):
    s_sum += max(a[i][c[0]],a[i][c[1]],a[i][c[2]])
      
  if s_sum > max_sum:
    max_sum = s_sum 

print(max_sum)