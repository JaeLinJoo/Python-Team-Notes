#오큰수

### 시간초과
n = int(input())
arr = list(map(int, input().split()))

def solution(n,arr):
    answer = []
    for i in range(n-1):
        if max(arr[i+1:])<=arr[i]:
            answer.append(-1)
            continue
        else:
            for j in range(i+1,n):
                if arr[i] < arr[j]:
                    answer.append(arr[j])
                    break
        
    answer.append(-1)
    return answer

answer = solution(n,arr)
for a in answer:
    print(a, end=' ')
    

## solution (ref: https://hongcoding.tistory.com/40)
import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = []
stack.append(0)
for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)


print(*answer)