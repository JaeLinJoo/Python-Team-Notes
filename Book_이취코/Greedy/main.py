# 그리디 
# 예제 문제 - 거스름돈 , 최소 동전
n=1260
count = 0

coin_type = [500, 100, 50, 10]

for coin in coin_type :
    count += n//coin
    n %= coin

print(count)
