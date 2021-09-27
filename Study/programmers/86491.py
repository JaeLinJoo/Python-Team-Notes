#weekly 8
# 최소 직사각형

def solution(sizes):
    answer = 0
    max_1, max_2 = 0, 0
    for size in sizes:
        x, y = sorted(size)
        if max_1<x:
            max_1 = x
        if max_2<y:
            max_2 = y
        
    answer = max_1*max_2
    
    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
