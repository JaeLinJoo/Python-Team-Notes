# 실전문제1 <미래도시>
############# mine ################
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
  a,b = map(int, input().split())
  graph[a].append((b,1))

x, k = map(int, input().split())

def dijkstra(start):
  distance[start]=0
  q = []
  heapq.heappush(q,(0,start))
  while q:
    dist, now = heapq.heappop(q)
    
    if dist > distance[now]:
      continue
    for j in graph[now]:
      cost = dist + j[1]

      if cost<distance[j[0]]:
        distance[j[0]]=cost
        heapq.heappush(q,(cost,j[0]))

dijkstra(1)
sk = distance[k]
dijkstra(k)
kx = distance[x]
result = sk + kx

if result >= INF :
  print(-1)
else:
  print(result)
  
######### solution ##########
# 플로이드 워셜의 전형적인 문제....

INF = int(1e9)

n,m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
  for b in range(1,n+1):
    if a==b:
      graph[a][b] = 0

for _ in range(m):
  a,b = map(int, input().split)
  graph[a][b] = 1
  graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance>=INF:
  print("-1")
else:
  print(distance)

