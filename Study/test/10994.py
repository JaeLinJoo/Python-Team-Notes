#별찍기 - 19
n = int(input())
stars = [[' ']*(n*4-3) for _ in range(n*4-3)] 

def make(n,point):
    if n == 1:
        stars[point][point] = '*'
        return 
    
    r = n*4-3
    for i in range(point,point+r):
        stars[point][i] = '*' #직사각형 젤 윗줄
        stars[point+r-1][i] = '*' #직사각형 젤 아랫줄

        stars[i][point] = '*' #직사각형 왼쪽
        stars[i][point+r-1] = '*' #오른쪽
    
    return make(n-1, point+2)

make(n,0)

for i in range(n*4-3):
    for j in range(n*4-3):
        print(stars[i][j], end='')
    print()
