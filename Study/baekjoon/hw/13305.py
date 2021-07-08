#주유소
import time
####### ↓↓↓↓↓↓↓시간초과↓↓↓↓↓↓↓
str1 = time.time()
from sys import stdin

n = int(input()) #도시갯수
dist = list(map(int,stdin.readline().split()))
oil_price = list(map(int,stdin.readline().split()))

min_city = n-1
end_city = n-1
dist_sum = 0
price_sum = 0
while True:
    if dist_sum == sum(dist):
        break
    
    min_p = min(oil_price[0:min_city])
    min_city = oil_price.index(min_p)
    price_sum += sum(dist[min_city:end_city]) * min_p
    dist_sum += sum(dist[min_city:end_city])
    end_city = min_city

print(price_sum)
print("첫번째 풀이 시간: ", time.time()-str1)
    
#### solution #########
str2 = time.time()
from sys import stdin

n = int(input()) #도시갯수
dists = list(map(int,stdin.readline().split()))
prices = list(map(int,stdin.readline().split()))

total = 0
min_price = prices[0]
for i in range(n-1):
    if min_price > prices[i]:
        min_price = prices[i]
    total += min_price * dists[i]

print(total)
print("두번째 풀이 시간: ", time.time()-str2)