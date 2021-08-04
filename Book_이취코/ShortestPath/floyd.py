INF = int(1e9)

# node의 개수 및 간선의 개수 입력받기
n = int(input())
m = int(input())

#2차원 리스트를 만들고, 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기자신->자기자신 비용 0으로 초기화
for a in range(1, n+1):
  for b in range(1, n+1):
    if a==b:
      graph[a][b] = 0

# 각 간선에 대한 정보 입력받아, 그래프 초기화
for _ in range(m):
  # A->B로 가는 비용: C
  a,b,c = map(int, input().split())
  graph[a][b] = c

#점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 수행 결과 출력
for a in range(1,n+1):
  for b in range(1,n+1):
    # 도달할 수 없는 경우
    if graph[a][b] == INF:
      print("INFINITY", end = " ")
    else:
      print(graph[a][b], end=" ")
  print()