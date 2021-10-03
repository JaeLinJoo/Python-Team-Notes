n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for e in graph[start]:
        if not visited[e]:
            dfs(graph, e, visited)

from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        s = queue.popleft()
        print(s, end=' ')
        for e in graph[s]:
            if not visited[e]:
                queue.append(e)
                visited[e] = True

visited = [False]*(n+1)
dfs(graph, v, visited)
print()
visited = [False]*(n+1)
bfs(graph, v, visited)