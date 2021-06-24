#큰 수 구성하기

#### ex) 655 3 / {6, 7, 7} => 77이 나와야 정답인데 607이 나옴
n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

len_max = len(str(n))
answer = 0
for i in range(len_max):
    for j in range(len(arr)):
        tmp = arr[j]*(10**(len_max-1-i))
        if answer + tmp <= n:
            answer += tmp
            break



######## solution ########
# product 사용 / .join(리스트) 사용
from itertools import product

N,K = map(int,input().split())
arr = list(map(str,input().split()))
length = len(str(N))

while(True):
    temp = list(product( arr, repeat=length))
    answer = []

    for i in temp :
        if int("".join(i)) <= N :
            answer.append(int("".join(i)))

    if len(answer)>= 1:
        print(max(answer))
        break
    else : 
        length -=1

