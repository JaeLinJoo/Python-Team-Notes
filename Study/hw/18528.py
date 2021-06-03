#### solution ######

from collections import deque
from sys import stdin

class queue(object):
    def __init__(self):
        self.q = deque()

    def push(self, item):
        self.q.append(item)

    def pop(self):
        if self.empty() != 1:
            return self.q.popleft()
        else:
            return -1

    def size(self):
        return len(self.q)

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.empty() != 1:
            return self.q[0]
        else:
            return -1

    def back(self):
        if self.empty() != 1:
            return self.q[-1]
        else:
            return -1


n = stdin.readline()
q = queue()
for _ in range(int(n)):
    run = list(stdin.readline().split())
    if run[0] == "push":
        q.push(int(run[1]))
    elif run[0] == "pop":
        print(q.pop())
    elif run[0] == "size":
        print(q.size())
    elif run[0] == "empty":
        print(q.empty())
    elif run[0] == "front":
        print(q.front())
    else:
        print(q.back())


########## ↓↓↓↓↓ 시간 초과 ↓↓↓↓↓ ##########
import sys

n = int(input())
q = []
res = []
for i in range(n):
  com = sys.stdin.readline().rstrip()
  if com.find('push') > -1:
    c = com.split()
    com, x = c[0],c[1]

  if com == 'push':
    q.append(x)
  elif com == 'pop':
    if len(q)==0:
      res.append(-1)
    else:
      res.append(q[0])
      q = q[1::]
  elif com == 'size':
    res.append(len(q))
  elif com == 'empty':
    if len(q) == 0:
      res.append(1)
    else:
      res.append(0)
  elif com == 'front':
    if len(q) == 0:
      res.append(-1)
    else:
      res.append(q[0])
  elif com == 'back':
    if len(q) == 0:
      res.append(-1)
    else:
      res.append(q[-1])

for r in res:
  print(r)

