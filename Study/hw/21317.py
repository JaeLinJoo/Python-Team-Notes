#징검다리 건너기

def jump(sum, start, bigJump, n, k):
    global res
    if start == n:
        res = min(res,sum)
        return res
    
    if start>n:
        return 
    
    jump(sum+energy[start][0], start+1, bigJump, n, k)
    jump(sum+energy[start][1], start+2, bigJump, n, k)

    if bigJump==False:
        jump(sum+k, start+3, True, n, k)

n = int(input())
energy = []
energy.append([0,0])
for _ in range(n-1):
    energy.append(list(map(int,input().split())))

k = int(input())
res = int(1e9)
jump(0,1,False, n, k)
print(res)


