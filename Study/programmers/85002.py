# weekly challenge 6
# 복서 정렬하기

def solution(weights, head2head):
    
    report = [] #각 선수별 기록
    n = len(weights)
    for i in range(n):
        win_cnt = 0
        lose_cnt = 0
        win_heavy = 0 #자기보다 무거운 선수 이긴 횟수
        for j in range(n):
            if i==j:
                continue
            if head2head[i][j] == 'W':
                win_cnt += 1
                if weights[i]<weights[j]:
                    win_heavy += 1
            elif head2head[i][j] == 'L':
                lose_cnt += 1
        if (win_cnt+lose_cnt)!=0:
            rate = win_cnt/(win_cnt+lose_cnt) #승률
        else:
            rate = 0
        report.append([-rate, -win_heavy, -weights[i], i])
    
    report.sort()
    answer = []
    for i in range(n):
        answer.append(report[i][3]+1)
    
    return answer


weights = [50,82,75,120]
head2head = ["NLWL","WNLL","LWNW","WWLN"]
print(solution(weights, head2head))

            



