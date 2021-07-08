# 진우의 달 여행 (Large)
# solution
from sys import maxsize, setrecursionlimit, stdin

def visitable(loc,cur_dir,next_dir):
    r, c = loc
    flag = (cur_dir != next_dir and 0<=c<m)
    return flag

def trip(loc,cur_dir,d):
    r, c = loc
    # 끝에 도달
    if r == n:
        return 0
    #찾은 값이 있는 경우, 탐색할 필요없음
    if d[r][c][cur_dir] != maxsize:
        return d[r][c][cur_dir]
    
    dirs = (-1,0,1)
    # enumerate : 열거형, 순서가 함께 나옴
    for next_dir, dc in enumerate(dirs):
        next_r, next_c = r+1, c+dc
        if visitable((next_r,next_c),cur_dir,next_dir):
            d[r][c][cur_dir] = min(d[r][c][cur_dir], trip((next_r,next_c),next_dir,d)+space[r][c])
        
    return d[r][c][cur_dir]

setrecursionlimit(2000)
n, m = map(int, input().split())
space = []
for i in range(n):
    space.append(list(map(int,stdin.readline().split())))

d = [[[maxsize] * 3 for _ in range(m)] for _ in range(n)]
res = maxsize

for i in range(m):
    for j in range(3):
        res = min(res, trip((0,i),j,d))

print(res)

