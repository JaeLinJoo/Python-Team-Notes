#조합

## 1. 라이브러리 사용
from itertools import combinations

print("라이브러리 사용 :",list(combinations([1,2,3,4],2)))

## 2. 재귀를 이용한 방법
"""
[idea] - dfs, 백트래킹과 유사함
* combination([0,1,2,3], 2) = ([0],combination([1,2,3], 1)) + ([1],combination([2,3], 1)) + ([2],combination([3], 1)))
"""
def rec_combinations(arr, n):
    result = []
    
    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        elem = arr[i]
        rest_arr = arr[i+1:]
        for c in rec_combinations(rest_arr, n-1):
            result.append([elem]+c)
    
    return result

print("재귀 사용 combinations: ", rec_combinations([1,2,3,4],2))
## 조합의 경우의 수를 구하고 싶은 경우
def choose(n, k): #nCk
    if k == 0:
        return 1
    elif n < k:
        return 0
    else:
        return choose(n-1, k-1) + choose(n-1, k)


## 3. generator , yield 사용
"""
yield :
제너레이터라는 객체를 통해서 함수를 호출할 때마다 하나씩 전달해준다.
순차적으로 한번에 처리하는 것이 아니라, 함수가 호출될 때마다 순차적으로 하나씩 처리해서 값을 반환해주는 것
반복횟수 만큼 호출이 가능하다.
"""
def gen_combinations(arr, r):
    for i in range(len(arr)):
        if r==1:
            yield [arr[i]]
        else:
            for next in gen_combinations(arr[i+1:], r-1): #arr[i+1:] → arr[i:] : 중복 조합
                yield [arr[i]]+next

print("제너레이터 yield 사용: ", list(gen_combinations([1,2,3,4],2)))
