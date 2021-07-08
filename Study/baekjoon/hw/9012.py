#괄호
t = int(input())

res = []

for i in range(t):
    line = input()
    l_cnt = 0 
    
    for l in line:
        if l == '(':
          l_cnt += 1
        elif l == ')' :
          l_cnt -= 1
        if l_cnt == -1:
          break
    
    if l_cnt == 0 :
        res.append('YES')
    else:
        res.append('NO')

for r in res:
    print(r)
