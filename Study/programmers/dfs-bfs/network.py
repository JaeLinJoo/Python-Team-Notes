n = int(input())
computers = [list(map(int, input().split())) for _ in range(n)]

def dfs(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1 and visited[connect]==False:
            dfs(n, computers, connect, visited)
            

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for com in range(n):
        if visited[com] == False:
            dfs(n, computers, com, visited)
            answer += 1
    return answer

print(solution(n,computers))