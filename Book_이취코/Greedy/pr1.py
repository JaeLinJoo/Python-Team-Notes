#<큰 수의 법칙>

##################### 나의 풀이 ###########################
N, M ,K = map(int,input().split())

array = list(map(int, input().split()))

array.sort(reverse=True)

# 반복되는 구간 횟수
repeat = M // (K+1)
# 나머지 
rmd = M% (K+1)

sum = 0
sum = (array[0]*K + array[1])*repeat + array[0]*rmd

print(sum)

# 아쉬운점 : N을 사용하지 않은 점.
##################### 책 풀이 ##############################
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m%(k+1)

result = (count)*first 
result += (m-count)*second

print(result)
