import sys 
input = sys.stdin.readline
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1
    while queue:
        s = queue.popleft()
        for e in graph[s]:
            if visited[e] == 0:
                visited[e] = -visited[s]
                queue.append(e)
            else:
                if visited[e] == visited[s]:
                    return False
    return True


k = int(input())

for _ in range(k):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    flag = True
    visited = [0]*(n+1)
    for v in range(1,n+1):
        if visited[v]==0:
            if not bfs(graph,v,visited):
                flag = False
                break
    
    print('YES' if flag else 'NO')


    

