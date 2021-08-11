#등굣길
m, n, l = map(int, input().split())
puddles = [list(map(int, input().split())) for _ in range(l)]

def solution(m, n, puddles):
    graph = [[0]*(m+1) for _ in range(n+1)]
    graph[1][1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1 and j==1:
                continue
            if [j,i] in puddles:
                graph[i][j] = 0
            else:
                graph[i][j] = graph[i-1][j] + graph[i][j-1]
    return graph[n][m]%1000000007

print(solution(m,n,puddles))
    


