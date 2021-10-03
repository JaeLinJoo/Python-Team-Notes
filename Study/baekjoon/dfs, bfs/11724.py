n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, start, visited):
    visited[start] = True

    for e in graph[start]:
        if not visited[e]:
            dfs(graph, e, visited)

from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        s = queue.popleft()    
        for e in graph[s]:
            if not visited[e]:
                queue.append(e)
                visited[e] = True

visited = [False]*(n+1)
cnt1 = 0
for v in range(1,n+1):
    if visited[v]:
        continue
    dfs(graph, v, visited)
    cnt1+=1

visited2 = [False]*(n+1)
cnt2 = 0
for v in range(1,n+1):
    if visited2[v]:
        continue
    bfs(graph, v, visited2)
    cnt2+=1

print(cnt1, cnt2)

