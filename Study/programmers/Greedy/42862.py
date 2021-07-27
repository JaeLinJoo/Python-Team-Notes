#체육복

n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))

def solution(n, lost, reserve):
    set_reserve = set(reserve)-set(lost)
    set_lost = set(lost)-set(reserve)
    for r in set_reserve:
        if r-1 in set_lost:
            set_lost = set_lost - {r-1}
        elif r+1 in set_lost:
            set_lost = set_lost - {r+1}
        
    return n-len(set_lost)

print(solution(n,lost,reserve))

    