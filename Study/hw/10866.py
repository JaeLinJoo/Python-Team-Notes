#덱
from collections import deque
from sys import stdin

class Deque(object):
    def __init__(self):
        self.q = deque()
    
    def push_front(self, x):
        self.q.appendleft(x)
    
    def push_back(self, x):
        self.q.append(x)
    
    def pop_front(self):
        if self.empty() != 1:
            return self.q.popleft()
        else:
            return -1
    
    def pop_back(self):
        if self.empty() != 1:
            return self.q.pop()
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
    
n = int(input())
q = Deque()
for _ in range(n):
    run = list(stdin.readline().split())
    if run[0] == 'push_front':
        q.push_front(int(run[1]))
    elif run[0] == 'push_back':
        q.push_back(int(run[1]))
    elif run[0] == 'pop_front':
        print(q.pop_front())
    elif run[0] == 'pop_back':
        print(q.pop_back())
    elif run[0] == 'size':
        print(q.size())
    elif run[0] == 'empty':
        print(q.empty())
    elif run[0] == 'front':
        print(q.front())
    else:
        print(q.back())
