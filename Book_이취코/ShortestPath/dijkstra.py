import sys

input = sys.stdin.readline
INF = int(1e9)

# node개수, 간선 개수 입력받기
n, m = map(int, input().split())
# 시작노드 입력 받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
# node 번호와 맞추기 위해 n+1개 만들고 0번쨰는 사용하지 않음
graph = [[] for i in range(n+1)]
# 방문한적 있는지 체크 목적의 리스트
visited = [False] * (n+1)
# 최단거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보 입력
for _ in range(m):
  a,b,c = map(int, input().split())
  # a -> b로 가는 비용:c
  graph[a].append((b,c))

#print(graph)

#방문하지 않은 노드 중, 가장 최단거리가 짧은 노드의 번호 반환
def get_smallest_node():
  min_value = INF 
  index = 0 # 가장 최단거리가 짧은 노드
  for i in range(1,n+1):
    if distance[i]<min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
  distance[start]=0
  visited[start] = True
  for j in graph[start]:
    distance[j[0]] = j[1]
  # 시작노드를 제외한 전체 n-1개의 노드에 대해 반복
  for i in range(n-1):
    now = get_smallest_node()
    visited[now] = True
    # 현재 노드와 연결된 다른 노드 확인
    for j in graph[now]:
      cost = distance[now]+ j[1]
      # 현재 노드를 거쳐서 다른 노드로 이동하는게 더 짧은 경우
      if cost < distance[j[0]]:
        distance[j[0]] = cost

dijkstra(start)

for i in range(1,n+1):
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])

