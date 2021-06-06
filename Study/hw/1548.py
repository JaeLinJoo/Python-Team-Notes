#부분 삼각 수열
from itertools import combinations

def sub_tri_seq(a):
  sub_seq = set(a)
  comb = list(combinations(a,3))
  for c in comb:
    c= list(c)
    c.sort()
    if c[0]+c[1]<=c[2]:
      sub_seq.discard(c[0])
  return sub_seq

def tri_seq(a):
  sub_seq = set()
  if len(a) > 3 :
    comb = list(combinations(a,3))
    for c in comb:
      c= list(c)
      c.sort()
      if c[0]+c[1]>c[2]:
        sub_seq.update(c)
    if len(sub_seq)>3:
      sub_seq = sub_tri_seq(sub_seq)
    return len(sub_seq)
  elif len(a)==3 :
    a.sort()
    if a[0]+a[1]>a[2]:
      return 3
    else:
      return 2
  else:
    return 1
  
  
n = int(input())
a = list(map(int,input().split()))

if n == 0:
  print(0)

res = tri_seq(a)
print(res)

