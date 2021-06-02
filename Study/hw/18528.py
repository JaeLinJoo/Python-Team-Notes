# 큐2

def queue(command,q):
  if command.find('push') > -1:
    c = command.split()
    com, x = c[0],c[1]
  com = command
  if com == 'push':
    q.append(x)
    return 
  elif com == 'pop':
    if len(q)==0:
      return -1
    else:
      res = q[0]
      q = q[1::]
      return res
  elif com == 'size':
    return len(q)
  elif com == 'empty':
    if len(q) == 0:
      return 1
    else:
      return 0
  elif com == 'front':
    if len(q) == 0:
      return -1
    else:
      return q[0]
  elif com == 'back':
    if len(q) == 0:
      return -1
    else:
      return q[-1]

import sys
import time
start = time.time()

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
      #print(-1)
      res.append(-1)
    else:
      res.append(q[0])
      q = q[1::]
      #print(res)
  elif com == 'size':
    #print(len(q))
    res.append(len(q))
  elif com == 'empty':
    if len(q) == 0:
      #print(1)
      res.append(1)
    else:
      #print(0)
      res.append(0)
  elif com == 'front':
    if len(q) == 0:
      #print(-1)
      res.append(-1)
    else:
      #print(q[0])
      res.append(q[0])
  elif com == 'back':
    if len(q) == 0:
      #print(-1)
      res.append(-1)
    else:
      #print(q[-1])
      res.append(q[-1])

for r in res:
  print(r)
  
print("time: ",time.time()-start)
  #res.append(queue(command))

#for r in res:
#  print(r)