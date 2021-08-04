#부족한 금액 계산하기

def solution(price, money, count):
    for i in range(1,count+1):
        money -= price*i
    
    if money >= 0:
        return 0
    else:
        return -money

p, m, c = map(int, input().split());

print(solution(p,m,c))