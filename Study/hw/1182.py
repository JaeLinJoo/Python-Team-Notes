#부분 수열의 합
n, tar = map(int, input().split())
sequence = list(map(int, input().split()))

from itertools import combinations

cnt = 0
for i in range(1,n+1):
    comb = combinations(sequence,i)
    for c in comb:
        if sum(list(c)) == tar:
            cnt += 1
    
print(cnt)
