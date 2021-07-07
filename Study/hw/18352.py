#특정 거리의 도시 찾기
import sys
import heapq
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
INF = int(1e9)

graph = [[] for i in range(n+1)]
distance =[INF]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q,(cost,i))

dijkstra(x)

if k in distance:
    for i in range(1,n+1):
        if distance[i] == k:
            print(i)
else:
    print(-1)
