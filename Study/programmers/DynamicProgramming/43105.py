#정수 삼각형

import sys
input = sys.stdin.readline
n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

def solution(triangle):
    n = len(triangle)
    for i in range(1,n):
        for j in range(i+1):
            if j==0:
                triangle[i][j] += triangle[i-1][j]
            elif j==i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] = max(triangle[i][j]+triangle[i-1][j-1],triangle[i][j]+triangle[i-1][j])
    
    return max(triangle[n-1])

print(solution(triangle))