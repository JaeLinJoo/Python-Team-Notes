k = int(input())

def solution(k):
    if k == 0:
        return 0
    if k == 1:
        return 1
    if k%2:
        return 1-solution(k//2)
    else:
        return solution(k//2)

print(solution(k-1))
