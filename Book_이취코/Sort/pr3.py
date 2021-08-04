# <두 배열의 원소 교체>

n,k = map(int, input().split())

array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

# 내림차순 정렬
array_a.sort()

# 오름차순 정렬
array_b.sort(reverse = True)

for i in range(k):
  #array_a[i] = array_b[i]  // 매우 큰 실수! : 꼭 b에 있는게 크지않음
  if array_a[i] < array_b[i]:
    array_a[i], array_b[i] = array_b[i], array_a[i]
  else :
    break

result = sum(array_a)

print(result)


