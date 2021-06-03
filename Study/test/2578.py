# 빙고
def check_sum(bingo):
  # 가로줄
  check = []
  check.append(sum(bingo[0]))
  check.append(sum(bingo[1]))
  check.append(sum(bingo[2]))
  check.append(sum(bingo[3]))
  check.append(sum(bingo[4]))

  # 세로줄
  check.append(sum(bingo[i][0] for i in range(5)))
  check.append(sum(bingo[i][1] for i in range(5)))
  check.append(sum(bingo[i][2] for i in range(5)))
  check.append(sum(bingo[i][3] for i in range(5)))
  check.append(sum(bingo[i][4] for i in range(5)))

  #대각선
  check.append(sum(bingo[i][i] for i in range(5)))
  check.append(sum(bingo[i][4-i]for i in range(5)))

  return check

bingo = []
for i in range(5):
  bingo.append(list(map(int,input().split())))

a = []
for i in range(5):
  a.append(list(map(int,input().split())))

cnt = 0 #사회자가 부르는 수 카운트
check = []

for m in range(5):
  for n in range(5):
    check = check_sum(bingo)
    if check.count(0)>2:
      break

    x = a[m][n]
    cnt += 1
    for i in range(5):
      for j in range(5):
        if bingo[i][j]==x:
          bingo[i][j] = 0
    
print(cnt)  
  
  
