# 우선순위 큐, 최소힙 이용한 dijkstra algorithm
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# node개수, 간선 개수 입력받기
n, m = map(int, input().split())
# 시작노드 입력 받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n+1)]
# 최단거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보 입력
for _ in range(m):
  a,b,c = map(int, input().split())
  # a -> b로 가는 비용:c
  graph[a].append((b,c))


def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q:
    # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
    dist, now = heapq.heappop(q)
    # 현재 노드가 이미 처리된 적있는 노드라면 무시
    # visited 리스트를 사용하는게 아니라 거리 비교를 통해서
    if dist > distance[now] :
      continue
    # 현재 노드와 인접한 다른 노드 확인
    for i in graph[now]:
      cost = dist + i[1]
      # 현재 노드 거쳐서 다른노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost, i[0]))

dijkstra(start)

for i in range(1,n+1):
  if distance[i] == INF :
    print("INFINITY")
  else:
    print(distance[i])
