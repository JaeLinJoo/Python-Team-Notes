#님 게임
n = int(input())
stones = list(map(int, input().split()))

def solution(n, stones):
    one_cnt = 0
    for s in stones:
        if s==1:
            one_cnt += 1
    if one_cnt == n:
        if n%2 == 0:
            return 'koosaga'
        else:
            return 'cubelover'
    else:
        if one_cnt>0 and one_cnt%2==0:
            for i in range(n):
                if stones[i] != 1:
                    stones[i] = 1
                    break
    x = 0
    for i in range(n):
        x ^= stones[i]
    if x == 0:
        return 'cubelover'
    else:
        return 'koosaga'

print(solution(n,stones))

