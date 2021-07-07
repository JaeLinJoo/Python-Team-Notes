#경로 찾기
import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
INF = int(1e9)
answer = [[INF]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            answer[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            answer[i][j] = min(answer[i][j], answer[i][k]+answer[k][j])
            
for i in range(n):
    for j in range(n):
        if answer[i][j] == INF:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()

