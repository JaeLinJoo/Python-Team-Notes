# 블랙잭
from itertools import combinations

n, m = map(int, input().split())
# 카드 정보
a = list(map(int, input().split()))

comb = list(combinations(a,3))

min = 1e9
result = 0
for c in comb :
  sum(c)
  sub = m-sum(c)
  if sub==0:
    result = sum(c)
    break
  if sub>0 and sub<min:
    min = sub
    result = sum(c)

print(result)