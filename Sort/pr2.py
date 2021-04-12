# <성적이 낮은 순서로 학생 출력하기>

n = int(input())

array = []
for i in range(n):
  name, score = map(str, input().split())
  array.append((name, score))

def setting(data):
  return data[1]

result = sorted(array, key=setting)

for i in range(n):
  print(result[i][0], end=' ')


#### solution ####
n = int(input())

array = []
for i in range(n):
  input_data = input().split()
  array.append((input_data[0], int(input_data[1])))

#key를 이용해, 점수를 기준으로 정렬
array = sorted(array, key= lambda student: student[1])

for student in array:
  print(student[0], end=' ')
