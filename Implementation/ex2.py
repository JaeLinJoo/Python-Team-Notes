# 예제2 <시각>
# mine

n = int(input())

count = 0
for i in range(n+1):
  for j in range(60):
    for k in range(60):
      if str(i).find('3')!=-1 or str(j).find('3')!=-1 or str(k).find('3')!=-1:
        count += 1

print(count)

# solution
h = int(input())

count = 0
for i in range(h+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        count += 1

print(count)
