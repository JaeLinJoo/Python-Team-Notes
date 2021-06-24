#큰 수 구성하기
n, k = map(int, input().split())
arr = list(map(int, input().split()))

def find(n, arr):
    arr.sort(reverse=True)
    for i in arr:
        if n >= i :
            return i



    