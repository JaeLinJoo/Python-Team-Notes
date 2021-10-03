import sys
input = sys.stdin.readline

def dfs(x,y):
    if 0<=x<h and 0<=y<w:
        if graph[x][y] == 1:
            graph[x][y] = 2
            dfs(x-1, y-1)
            dfs(x-1, y)
            dfs(x-1, y+1)
            dfs(x, y-1)
            dfs(x, y+1)
            dfs(x+1, y-1)
            dfs(x+1, y)
            dfs(x+1, y+1)
            return True
        return False

while True:
    w, h = map(int, input().split())
    if w == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    result = 0
    for i in range(h):
        for j in range(w):
            if dfs(i,j):
                result += 1
        
    print(result)

