# [1차] 프렌즈 4블록

#solution 참고

#지워지는 블록의 개수
def popping(m, n ,board):
    pop_set = set()
    for i in range(1,n):
        for j in range(1,m):
            if board[i][j] == board[i-1][j] == board[i][j-1] == board[i-1][j-1] != ' ':
                pop_set |= set([(i, j), (i-1, j-1), (i-1, j), (i, j-1)])

    for i, j in pop_set:
        board[i][j] = 0

    for i, row in enumerate(board):
        empty = [' ']*row.count(0)
        board[i] = empty + [block for block in row if block!=0]

    return len(pop_set)

def solution(m, n, board):
    answer = 0
    b = list(map(list, zip(*board)))
    while True:
        pop = popping(m, n, b)
        if pop == 0:
            return answer
        answer += pop

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
        