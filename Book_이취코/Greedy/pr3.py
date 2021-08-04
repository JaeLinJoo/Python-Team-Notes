# <1이 될 때 까지>
########### 내 풀이 #########
import time

n, k = map(int, input().split())
start_time = time.time()
count = 0
while True:
  if n==1:
    break
  elif n%k == 0 :
    n //= k
    count += 1
  else:
    n -= 1
    count += 1

end_time = time.time()
print(count)
print("WorkingTime: {} sec".format(end_time-start_time))

############ 책 풀이 ##################
n, k = map(int, input().split())
start_time2 = time.time()

result = 0 

while n>=k:
  while n%k!=0:
    n -= 1
    result += 1
  n //= k
  result += 1

while n>1:
  n -= 1
  result += 1

end_time2 = time.time()
print(result)
print("WorkingTime2: {} sec".format(end_time2-start_time2))

#################### 책 풀이 2 ###################
n, k = map(int, input().split())
start_time3 = time.time()

result = 0 

while True:
  target = (n//k)*k
  result += (n-target)
  n = target

  if n<k:
    break
  result += 1
  n //= k

result += (n-1)

end_time3 = time.time()
print(result)
print("WorkingTime3: {} sec".format(end_time3-start_time3))