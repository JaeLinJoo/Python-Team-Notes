#스티커
t = int(input())
for i in range(t):
    n = int(input())
    sticker = []
    for j in range(2):
        sticker.append(list(map(int, input().split())))
    d = [[0]*100001 for _ in range(2)]
    
    d[0][0], d[1][0] = 0, 0
    d[0][1], d[1][1] = sticker[0][0], sticker[1][0]

    for k in range(2,n+1):
        d[0][k] = max(d[1][k-1], d[1][k-2]) + sticker[0][k-1]
        d[1][k] = max(d[0][k-1], d[0][k-2]) + sticker[1][k-1]
    
    res = max(d[0][n],d[1][n])
    print(res)