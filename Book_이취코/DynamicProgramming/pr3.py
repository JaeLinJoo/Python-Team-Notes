# <실전문제> 바닥공사

n = int(input())

d = [0]*10001

d[1] = 1
d[2] = 3

for i in range(3,n+1):
  d[i] = d[i-1] + d[i-2]*2

result = d[n]%796796

print(result)


# solution
for i in range(3,n+1):
  d[i] = (d[i-1] + d[i-2]*2 ) %796796

print(d[n])
