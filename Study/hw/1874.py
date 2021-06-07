#스택 수열
###### solution 참고함
from sys import stdin

n = int(stdin.readline().rstrip())
stack = []
oper = []
cnt = 1 #stack에 넣을 값
temp = True #수열을 만들 수 있는 없는지의 여부

for i in range(n):
    tar = int(stdin.readline().rstrip())
    while cnt<=tar: #스택에 쌓기
        stack.append(cnt)
        oper.append('+')
        cnt += 1
    if stack[-1] == tar: 
        stack.pop()
        oper.append('-')
    else:
        temp = False

if temp == False:
    print('NO')
else:
    for op in oper:
        print(op)