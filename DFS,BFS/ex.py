n, m = map(int, input().split())
graph = []
#(1,1)로 시작
graph.append([])
for i in range(n):
  graph.append(list(map(int,input())))

print(graph)
print(graph[1][1])
