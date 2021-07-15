#순열 (permutations)

## 1. 라이브러리 이용
from itertools import permutations

###permutations(반복 가능한 객체, r) r: 몇개씩 묶을 건지
for i in permutations([1,2,3,4],2):
    print(i, end=" ")

## 2. 재귀를 이용한 방법
"""
[idea] - dfs, 백트래킹과 유사함
permutation([0,1,2,3], 2) = ([0],permutation([1,2,3], 1)) + ([1],permutation([0,2,3], 1)) + ([2],permutation([0,1,3], 1))+ ([3],permutation([0,1,2], 1))
"""
def rec_permutaions(arr, n):
    result = []

    if n == 0 :
        return [[]]
    
    for i, elem in enumerate(arr):
        for p in rec_permutaions(arr[:i]+arr[i+1:],n-1):
            result += [[elem]+p]
    
    return result

## 3. yield 사용
def gen_permutaions(arr, n):
    if n == 1:
        yield [arr[i]]
    else:
        for next i in gen_permutaions(arr[:i]+arr[i+1:], n-1):
            yield [arr[i]] + next