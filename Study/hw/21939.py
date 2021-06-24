#문제 추천 시스템 version1
### 시간 초과. 이유찾지 못함... ㅜㅜ
import heapq
from sys import stdin

class system(object):
    def __init__(self):
        self.q = []
    
    def recommend(self,x):
        if x == -1:
            return self.q[0]
        else:
            self.q.sort()
            return self.q[-1]

    def add(self,p,l):
        heapq.heappush(self.q,(l,p))
    
    def solved(self,p):
        for i in range(len(self.q)):
            if self.q[i][1] == p:
                self.q.pop(i)
                break

q = system()    
n = int(input())
for i in range(n):
    p,l = map(int, stdin.readline().split())
    q.add(p,l)
m = int(input())
for i in range(m):
    command = list(stdin.readline().split())
    if command[0] == 'recommend':
        ans = q.recommend(int(command[1]))
        print(ans[1])
    elif command[0] == 'add':
        q.add(int(command[1]),int(command[2]))
    else:
        q.solved(int(command[1]))
                
