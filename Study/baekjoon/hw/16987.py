#계란으로 계란치기
#백트래킹 잘 모르겠음..

def breakEgg(eggs, current):
    n = len(eggs)
    global res

    if current == n :
        cnt = 0 
        for i in range(n):
            if eggs[i][0] <= 0:
                cnt += 1
        res = max(res,cnt)
        return 
    
    if eggs[current][0]<=0:
        breakEgg(eggs, current+1)
    else:
        flag = False
        for i in range(n):
            if i==current or eggs[i][0]<=0:
                continue
            eggs[current][0] -= eggs[i][1]
            eggs[i][0] -= eggs[current][1]
            flag = True
            breakEgg(eggs, current+1)
            eggs[current][0] += eggs[i][1]
            eggs[i][0] += eggs[current][1]
        if not flag:
            breakEgg(eggs, current+1)
    

n = int(input())
eggs = [list(map(int,input().split())) for _ in range(n)]

res = 0
breakEgg(eggs,0)
print(res)
