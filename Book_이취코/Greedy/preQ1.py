# 모험가 길드
n = int(input())
data = list(map(int, input().split()))

data.sort()

count = 0 # 그룹 내 길드원 수
result = 0 # 그룹 수

for i in data:
  count += 1
  if i<=count :
    result += 1
    count = 0

print(result)

# solution
# 다시 한번 해봐야할 것 .

