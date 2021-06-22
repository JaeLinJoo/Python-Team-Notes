# 설탕배달

n = int(input())

d = [2000] * (n+1)
arr = [3,5]

d[0] = 0
for i in range(2):
    for j in range(arr[i],n+1):
        if d[j-arr[i]]!=2000:
            d[j] = min(d[j], d[j-arr[i]]+1)

if d[n] == 2000 or d[n]==0:
    print(-1)
else:
    print(d[n])