# 한윤정 이탈리아 아이스크림
### ↓↓↓↓↓↓↓↓↓↓시간초과↓↓↓↓↓↓↓↓↓
from itertools import combinations
n, m = map(int,input().split())

no_comb = []
for i in range(m):
    no_comb.append(list(map(int,input().split())))

cnt = 0
icecream = [i for i in range(1,n+1)]
ice_comb = combinations(icecream, 3)

for ices in ice_comb:
    flag = True
    for no in no_comb:
        if no[0] in ices and no[1] in ices:
            flag = False
            break
    if flag:
        cnt+=1
    
print(cnt)

### ↓↓↓↓↓↓↓↓↓↓솔루션↓↓↓↓↓↓↓↓↓

cnt = 0 
n, m = map(int, input().split())
if n<3 :
    print(cnt)
else:
    no_mix = {i:[] for i in range(1,n+1)}
    for _ in range(m):
        x, y = map(int,input().split())
        no_mix[x].append(y)
        no_mix[y].append(x)
    
    for i in range(1,n+1):
        for j in range(i+1, n+1):
            if j in no_mix[i]:
                continue
            for k in range(j+1,n+1):
                if k in no_mix[i] or k in no_mix[j]:
                    continue
                cnt += 1

    print(cnt)