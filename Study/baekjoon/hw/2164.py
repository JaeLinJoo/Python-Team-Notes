#카드2
from collections import deque

n = int(input())
queue = deque()

for i in range(n):
    queue.append(i+1)

while len(queue)>1:
    # 제일 위 카드 버림
    queue.popleft()
    queue.append(queue.popleft())

print(queue.pop())


