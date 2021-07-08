# 다리놓기
import math

t = int(input())
cnt = [0]*t

for i in range(t):
  n, m = map(int,input().split())
  cnt[i] = math.comb(m,n)

for c in cnt:
  print(c)