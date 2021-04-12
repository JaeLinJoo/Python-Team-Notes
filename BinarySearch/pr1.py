# <문제1> 부품 찾기
# mine

n = int(input())
array = list(map(int, input().split()))

m = int(input())
req = list(map(int, input().split()))

# 내림차순 정렬
array = sorted(array)
print(array)
print(req)

def binary_search(array, target, start, end):
  if start>end:
    return 'no'
  
  mid = (start+end)//2
  if target == array[mid]:
    return 'yes'
  elif target < array[mid]:
    return binary_search(array, target, start, mid-1)
  else:
    return binary_search(array, target, mid+1, end)
  
for i in range(m):
  print(binary_search(array, req[i], 0, n-1), end=' ')

######### solution <계수 정렬> #######

n = int(input())
array = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
  array[int(i)] = 1

m = int(input())
x = list(map(int, input().split())

for i in x:
  if array[i]==1:
    print('yes', end=' ')
  else:
    print('no', end=' ')

########### solution <집합 자료형> ##########
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
  if i in array:
    print('yes', end = ' ')
  else:
    print('no', end=' ')
  


