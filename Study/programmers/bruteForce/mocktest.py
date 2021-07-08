def solution(answers):
    answer = []
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    
    cnt = [0,0,0]
    size = len(answers)
    for i in range(size):
        if answers[i] == num1[i%len(num1)]:
            cnt[0] += 1
        if answers[i] == num2[i%len(num2)]:
            cnt[1] += 1
        if answers[i] == num3[i%len(num3)]:
            cnt[2] += 1
    
    max_cnt = max(cnt)
    for i in range(3):
        if cnt[i] == max_cnt:
            answer.append(i+1)
        
    return answer

answers = list(map(int,input().split()))
answer = solution(answers)
print(answer)