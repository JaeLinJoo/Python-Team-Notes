# 신입사원
## 결국 구글링.. 
#### 한쪽만 비교하면 되는 문제였음..
#### 입력수가 많을 때는 sys로 입력받기
import sys

t = int(input())
count = [0]*t
for i in range(t):
  cnt = 1
  n = int(input())
  case = [] #테스트 케이스
  for j in range(n):
    case.append(list(map(int,sys.stdin.readline().split())))

  case.sort() # 서류기준 오름차순
  min = case[0][1]

  for k in range(1,n):
    if min > case[k][1] :
      cnt += 1
      min = case[k][1]
  
  count[i]=cnt

for i in range(t):
  print(count[i])