#Four Squares
import math 

n = int(input())
d = [5]*(n+1)

d[1] = 1
for i in range(2,n+1):
    if math.sqrt(i)%int(math.sqrt(i)) == 0:
        d[i] = 1
        continue
    else:
        sqrt = math.ceil(math.sqrt(i))
        for j in range(1,sqrt):
            d[i] = min(d[i],d[i-1]+1,d[i-j**2]+d[j**2])

print(d[n])