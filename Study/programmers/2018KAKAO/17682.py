# [1차] 다트게임

dartResult = input()

def solution(dartResult):
    point = []
    for i,r in enumerate(dartResult):
        #BONUS
        if r=='S':
            continue
        elif r =='D':
            point[-1] = point[-1]**2
        elif r == 'T':
             point[-1] =  point[-1]**3
        #OPTION
        elif r == '*':
            point[-1] =  point[-1]*2
            if len(point) > 1:
                point[-2] =  point[-2]*2
        elif r == '#':
            point[-1] =  point[-1]*(-1)
        else:
            if dartResult[i+1] == '0':
                continue
            if i!=0 and r=='0' and dartResult[i-1]=='1':
                point.append(10)    
            else:
                point.append(int(r))

    answer = sum(point)
    return answer

print(solution(dartResult))

#다른사람코드- 좀 더 깔끔하게 할 수 있음
def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)
