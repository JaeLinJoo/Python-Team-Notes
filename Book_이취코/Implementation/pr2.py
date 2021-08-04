# 실전문제2 <게임 개발>
###### solution 참고 #########
n, m = map(int, input().split())
# 현재 x*y위치, 방향
x, y, direction = map(int, input().split())

# 방문한 이력 기록할 맵
visit = [[0]*m for _ in range(n)]
# 현재 위치 방문 기록 업데이트
visit[x][y] = 1

# 주어진 map 정보에 따른 업데이트
info = []
for i in range(n):
  info.append(list(map(int, input().split())))

    #  북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left() :
  global direction
  # 현재 방향에서 왼쪽으로 회전
  # [0: 북, 1:동, 2:남, 3:서]
  direction -= 1
  if direction==-1:
    direction =3 
  
# 방문한 칸 수
count = 1
#회전한 횟수
turn_count = 0

while True:
  turn_left()
  
  nx = x + dx[direction]
  ny = y + dy[direction]

  # 방문한 적 없고 육지인 곳
  if visit[nx][ny]==0 and info[nx][ny]==0:
    x = nx
    y = ny
    # 방문 기록
    visit[x][y] = 1
    count += 1
    turn_count = 0
    continue
  
  else:
    turn_count += 1

  # 모든 방향에서 움직일 곳이 없을 때
  if turn_count==4:
    # 뒤로 한칸 이동
    nx = x - dx[direction]
    ny = y - dy[direction]
    # 바다가 아닐 경우
    if info[nx][ny] == 0 :
      x = nx
      y = ny
    # 바다일 경우
    else :
      break    
    turn_count = 0 

print(count)








