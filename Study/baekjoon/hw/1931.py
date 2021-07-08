#회의실 배정
### 솔루션 참고
##### 끝나는 시간, 시작시간 순으로 오름차순 정렬 
from sys import stdin

n = int(stdin.readline().rstrip())
schedule = [list(map(int, stdin.readline().split())) for _ in range(n)]

schedule = sorted(schedule, key = lambda s:(s[1],s[0])) 
last = 0
cnt = 0
for s,e in schedule:
    if s>=last:
        cnt += 1
        last = e

print(cnt)
