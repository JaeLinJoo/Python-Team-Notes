#동전 0 
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
cnt = 0
coins.reverse()

for c in coins:
    if k == 0:
        break
    if c > k:
        continue
    else:
        cnt += k//c
        k = k%c

print(cnt)
    