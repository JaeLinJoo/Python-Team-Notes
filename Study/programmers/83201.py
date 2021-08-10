#위클리챌린지 2주차
n = int(input())
scores = [list(map(int, input().split())) for _ in range(n)]

def grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80 and avg < 90:
        return 'B'
    elif avg >= 70 and avg < 80:
        return 'C'
    elif avg >= 50 and avg < 70:
        return 'D'
    else:
        return 'F'

def solution(scores):
    answer = ''
    n = len(scores)
    my_scores = [[]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            my_scores[j].append(scores[i][j])

    for i in range(n):
        cnt = n
        sum_scores = sum(my_scores[i])
        avg = 0
        for j in range(n):
            if i==j:
                if my_scores[i][j] == max(my_scores[i]) or my_scores[i][j] == min(my_scores[i]):
                    if my_scores[i].count(my_scores[i][j]) > 1:
                        continue
                    else:
                        cnt -= 1
                        sum_scores -= my_scores[i][j]

        avg = sum_scores/cnt
        answer += grade(avg)

    return answer

print(solution(scores))

##### 참고 ##### 
stu_scores = list(map(list, zip(*scores)))
print(stu_scores)