# 상어 초등학교
import sys
input = sys.stdin.readline

n = int(input())

def placement(n):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    graph = [[0]*n for _ in range(n)]
    like_dict = {}
    for i in range(n*n):
        _input = list(map(int, input().split()))
        like_dict[_input[0]] = _input[1:]

        rec_x, rec_y = 0, 0 #최종 추천 자리
        max_like, max_empty = -1, -1 #인접한 자리 중 좋아하는 학생 수, 빈칸 수

        for i in range(n):
            for j in range(n):
                if graph[i][j] == 0:
                    like_cnt, empty_cnt = 0, 0
                    for k in range(4):
                        nx = i+dx[k]
                        ny = j+dy[k]
                        if 0<=nx and nx<n and 0<=ny and ny<n:
                            if graph[nx][ny] in _input:
                                like_cnt += 1
                            if graph[nx][ny] == 0:
                                empty_cnt += 1

                    if max_like < like_cnt or (max_like == like_cnt and max_empty < empty_cnt):
                        rec_x, rec_y = i, j
                        max_like = like_cnt
                        max_empty = empty_cnt
        graph[rec_x][rec_y] = _input[0]
    
    return graph, like_dict

def satisfaction(n):
    graph, like_dict = placement(n)
    result = 0
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    for i in range(n):
        for j in range(n):
            cnt = -1
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx and nx<n and 0<=ny and ny<n:
                    if graph[nx][ny] in like_dict[graph[i][j]]:
                        cnt+=1

            if cnt>-1 :
                result += 10 ** cnt
    return result

print(satisfaction(n))