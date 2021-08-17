#위클리 챌린지 3주차

n = int(input())
game_board = [list(map(int, input().split())) for _ in range(n)]
table = [list(map(int, input().split())) for _ in range(n)]

def dfs(x,y,graph,mode,puzzle):
    n = len(graph)
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return []

    if graph[x][y] == mode:
            if puzzle != []:
                puzzle.append((x-puzzle[0][0],y-puzzle[0][1]))
            else :
                puzzle.append((x,y))
            graph[x][y] = 2
            dfs(x-1,y,graph,mode,puzzle)
            dfs(x+1,y,graph,mode,puzzle)
            dfs(x,y-1,graph,mode,puzzle)
            dfs(x,y+1,graph,mode,puzzle)
            return puzzle
    
    return []

def rotate(puzzle):
    for i,p in enumerate(puzzle):
        puzzle[i] = (-p[1],p[0])
    puzzle.sort()
    ix = 0-puzzle[0][0]
    iy = 0-puzzle[0][1]
    for i,p in enumerate(puzzle):
        puzzle[i] = (p[0]+ix,p[1]+iy)
    return puzzle

def solution(game_bard, table):
    n = len(game_bard)
    board_puzzles = []
    table_puzzles = []
    for i in range(n):
        for j in range(n):
            puzzle = dfs(i,j,game_bard,0,[])
            if puzzle != []:
                puzzle[0] = (0,0)
                board_puzzles.append(sorted(puzzle))

    for i in range(n):
        for j in range(n):
            puzzle = dfs(i,j,table,1,[])
            if puzzle != []:
                puzzle[0] = (0,0)
                table_puzzles.append(sorted(puzzle))

    cnt = 0
    for tp in table_puzzles:
        if tp in board_puzzles:
            cnt += len(tp)
            board_puzzles.pop(board_puzzles.index(tp))
            continue
        else:
            for i in range(3):
                tp = rotate(tp)
                if tp in board_puzzles:
                    cnt += len(tp)
                    board_puzzles.pop(board_puzzles.index(tp))
                    break

    return cnt


print(solution(game_board,table))

