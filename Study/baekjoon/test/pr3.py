#최소, 최대 2

# 테스트 케이스의 개수
t = int(input())

result = []
for i in range(t):
  n = int(input())
  array = list(map(int, input().split()))
  result.append((min(array), max(array)))

# print
for i in range(t):
  print(result[i][0], result[i][1])
