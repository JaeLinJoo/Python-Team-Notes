#행렬
n, m = map(int,input().split())
# N x M 행렬
a = []
b = [] 
for i in range(n):
  a.append(list(map(int,input())))

for i in range(n):
  b.append(list(map(int,input())))

def change(p,q,a):
  for j in range(q,q+3):
    for i in range(p, p+3):
      a[i][j] = 1-a[i][j]

cnt = 0 # 연산 횟수
for i in range(0,n-2):
  for j in range(0,m-2):
    if a[i][j]!=b[i][j]:
      change(i,j,a)
      cnt += 1

if(a!=b):
  print(-1)
else:
  print(cnt)


#################↓↓↓↓↓↓↓↓↓↓↓↓런타임 에러↓↓↓↓↓↓↓↓↓↓↓↓###################

#행렬
import sys

n, m = map(int,input().split())
# N x M 행렬
a = []
b = [] 
for i in range(n):
  a.append(sys.stdin.readline().rstrip())

for i in range(n):
  b.append(sys.stdin.readline().rstrip())

cnt = 0

if a==b: # 애초에 같은 경우
  print(cnt)

if n<3 or m<3: # 3*3 부분행렬을 가질 수 없는 경우
  print(-1)

p = 0 
q = 0
while True:
  
  if a==b:
    break

  for j in range(q,q+3):
    for i in range(p, p+3):
      if a[i][j] == '0':
        a[i] = a[i][0:j] + '1' + a[i][j+1:m]
      else:
        a[i] = a[i][0:j] + '0' + a[i][j+1:m]
  
  cnt += 1

  if q!=m-2:
    q += 1
  else :
    if p!=n-2:
      p += 1
    else: 
      print(-1)
      break

print(cnt)
