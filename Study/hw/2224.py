#명제 증명
import sys
input = sys.stdin.readline
n = int(input())
p = set()
graph = []

for i in range(n):
    prop = input().rstrip()
    pre, post = prop[0], prop[-1]
    p.update([pre, post])
    graph.append((pre,post))

p = list(p)
p.sort()
INF = int(1e9)
answer = [[INF]*len(p) for _ in range(len(p))]

for g in graph:
    answer[p.index(g[0])][p.index(g[1])] = 1

for k in range(len(p)):
    for i in range(len(p)):
        for j in range(len(p)):
            answer[i][j] = min(answer[i][j], answer[i][k]+answer[k][j])

res = []
for i in range(len(p)):
    for j in range(len(p)):
        if i!=j and answer[i][j] != INF:
            res.append((i,j))

print(len(res))
res.sort()
for r in res:
    print(p[r[0]],"=>",p[r[1]])

