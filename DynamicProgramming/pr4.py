# < 실전문제 > 효율적인 화폐구성

n, m = map(int, input().split())

a = []
for i in range(n):
  a.append(int(input()))

a.sort()

d = [10001] * (m+1)
d[0] = 0

for i in range(1, m+1):
  for j in range(0, n):
    if i>a[j]:
      d[i] = min(d[i], d[i-a[j]]+1)
    else:
      continue

if d[m] > 10000:
  print(-1)
else:
  print(d[m])

############### solution #############
for i in range(n):
  for j in range(a[i],m+1):
    if d[j-a[i]] != 10001 :
      d[j] = min(d[j], d[j-a[i]]+1)

if d[m] == 10001 :
  print(-1)
else:
  print(d[m])

  


