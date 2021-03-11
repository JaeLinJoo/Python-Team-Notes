# 실전문제 1 < 왕실의 나이트 >

###### mine ######
now = input()
x = int(now[1])
y = ord(now[0])

dx = [-2,-2,2,2,-1,-1,1,1]
dy = [-1,1,-1,1,-2,2,-2,2]

count = 0

for i in range(8):
  nx = x + dx[i]
  ny = y + dy[i]
  
  if nx > 0 and nx < 9 and ny >= ord('a') and ny <= ord('h'):
    count += 1

print(count)

####### solution ########
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]))-int(ord('a'))+1

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result = 0
for step in steps:
  next_row = row + step[0]
  next_col = column + step[1]

  if next_row>=1 and next_row<=8 and next_col>=1 and next_col<=8:
    result += 1

print(result)