#선수과목(Prerequisite)
##위상정렬 
from collections import deque

n, m = map(int, input().split())
pre = [[] for _ in range(n+1)]
degree = [0]*(n+1)
time = [0]*(n+1)
dq = deque()

for _ in range(m):
    a, b = map(int, input().split())
    pre[a].append(b)
    degree[b] += 1

for i in range(1,n+1):
    if degree[i] == 0:
        dq.append((i,1))

while dq:
    index, t = dq.popleft()
    time[index] = t
    for j in pre[index]:
        degree[j] -= 1

        if degree[j] == 0:
            dq.append((j,t+1))

for t in range(1,len(time)):
    print(time[t], end = ' ')