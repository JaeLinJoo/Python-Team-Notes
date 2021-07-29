#2019 카카오 개발자 겨울 인턴십
# 크레인 인형뽑기

import sys
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
moves = list(map(int, input().split()))

def solution(board, moves):
    basket = []
    result = 0
    n = len(board)
    for m in moves:
        for i in range(n):
            if board[i][m-1] == 0:
                continue
            basket.append(board[i][m-1])
            board[i][m-1] = 0
            break
        if len(basket)>1 :
            if basket[-1] == basket[-2]:
                result += 2
                basket.pop()
                basket.pop()

    return result

print(solution(board, moves))
        
