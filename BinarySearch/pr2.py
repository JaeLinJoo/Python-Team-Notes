# <문제2> 떡볶이 떡 만들기
# 문제 이해 실패, 솔루션 보고 이해함

n, m = map(int, input().split())
array = list(map(int, input().split()))

#1cm 단위로 끊음, index는 자르는 위치라고 생각하기
start = 0
end = max(array)

result = 0
while start<=end :
  total = 0
  mid = (start+end)//2
  for x in array :
    if x > mid :
      total += x-mid
  
  if total < m:
    end = mid - 1
  
  else :
    result = mid # 최대한 덜 잘랐을 때가 정답이므로...?
    start = mid + 1

print(result)