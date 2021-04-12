# 실전문제 1 <음료수 얼려먹기>
# solution

n, m = map(int, input().split())
graph = []

for i in range(n):
  graph.append(list(map(int, input())))

def dfs(x,y):
  # 얼음틀 벗어나는 경우 제외
  if x<=-1 or x>=n or y<=-1 or y>=m:
    return False
  
  if graph[x][y] == 0 :
    graph[x][y] = 1
    # 해당 좌표에서 상,하,좌,우 모두 방문
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True
  
  return False

# 한번에 나올 수 있는 아이스크림 수
result = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j)==True:
      result += 1

print(result)
