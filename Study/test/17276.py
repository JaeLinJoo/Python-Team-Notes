#배열 돌리기
#solution 참고
def rotate(arr,dir,n):
    cnt = abs(dir)//45 #회전 횟수
    center = (n+1)//2 - 1
    #시계방향
    if dir > 0:
        for _ in range(cnt):
            prev_list = []

            for i in range(n):#주대각선
                prev_list.append(arr[i][i])
            
            for i in range(n): #주대각선 => 가운데열
                prev_temp = arr[i][center]
                arr[i][center] = prev_list[i]
                prev_list[i] = prev_temp

            for i in range(n): #가운데열 => 부대각선
                prev_temp = arr[i][n-1-i]
                arr[i][n-1-i] = prev_list[i]
                prev_list[i] = prev_temp
            
            for i in range(n): #부대각선 => 가운데행
                prev_temp = arr[center][n-1-i]
                arr[center][n-1-i] = prev_list[i]
                prev_list[i] = prev_temp
            
            for i in range(n): #가운데 행 => 주 대각선
                arr[i][i] = prev_list[n-1-i]
                
    #반시계방향
    if dir < 0:
        for _ in range(cnt):
            prev_list = []

            for i in range(n):#주대각선
                prev_list.append(arr[i][i])
            
            for i in range(n): #주대각선 => 가운데행
                prev_temp = arr[center][i]
                arr[center][i] = prev_list[i]
                prev_list[i] = prev_temp

            for i in range(n): #가운데행 => 부대각선
                prev_temp = arr[n-1-i][i]
                arr[n-1-i][i] = prev_list[i]
                prev_list[i] = prev_temp
            
            for i in range(n): #부대각선 => 가운데열
                prev_temp = arr[n-1-i][center]
                arr[n-1-i][center] = prev_list[i]
                prev_list[i] = prev_temp
            
            for i in range(n): #가운데열 => 주 대각선
                arr[n-1-i][n-1-i] = prev_list[i]

t = int(input())

for _ in range(t):
    n, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    rotate(arr,d,n)

    for i in range(n):
        for j in range(n):
            print(arr[i][j], end = ' ')
        print()