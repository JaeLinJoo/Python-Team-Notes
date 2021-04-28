# 실전문제2 <전보>
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
  x,y,z = map(int, input().split())
  graph[x].append((y,z))

def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    if dist > distance[now]:
      continue
    for j in graph[now]:
      cost = dist + j[1]
      if cost < distance[j[0]]:
        distance[j[0]] = cost
        heapq.heappush(q,(cost,j[0]))

dijkstra(c)
count = 0
total_time = 0
for dist in distance:
  if dist < INF and dist!=0:
    count += 1
    # 동시에 보내지므로, 가장 맥스 시간을 출력하면됨!!
    total_time = max(total_time, dist)

print(count, total_time)
