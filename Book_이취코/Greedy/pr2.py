# < 숫자 카드 게임 >
n, m = map(int, input().split())

data = list([0]*m for _ in range(n))
for i in range(n):
  data[i] = list(map(int, input().split()))

row_min = []
for i in range(n):
  data[i].sort()
  row_min.append(data[i][0])

row_min.sort()
result = row_min[-1]
#print("mine_data: ",data)
print(result)


################### 책풀이 #######################
n, m = map(int, input().split())

data = list([0]*m for _ in range(n))

result = 0
for i in range(n):
  data = list(map(int, input().split()))

  min_value = min(data)

  result = max(result, min_value)

#print("solution: ",data)
print(result)

