#연구소
import sys
input = sys.stdin.readline
import copy 

n,m = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

answer = 0

virus_list = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            virus_list.append([i,j])

def select_wall(start, count):
    global answer
    if count == 3:
        selected_board = copy.deepcopy(board)
        for x,y in virus_list:
            spread_virus(x,y,selected_board)
        safe_count = sum(i.count(0) for i in selected_board)
        answer = max(answer, safe_count)
        return True
    else:
        for i in range(start,n*m):
            x = i//m 
            y = i%m 
            if board[x][y] == 0:
                board[x][y] = 1
                select_wall(i,count+1)
                board[x][y] = 0

def spread_virus(x,y,selected_board):
    if selected_board[x][y] == 2:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if selected_board[nx][ny] == 0:
                    selected_board[nx][ny] = 2
                    spread_virus(nx,ny,selected_board)

select_wall(0,0)
print(answer)