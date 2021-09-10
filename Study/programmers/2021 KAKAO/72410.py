#신규 아이디 추천

def solution(new_id):
    answer = ''
    #1단계 : 소문자 치환
    answer = new_id.lower()
    #2단계 : 특수문자 빼기
    for w in answer:
        if w.isalpha() or w.isdecimal():
            continue
        elif w == '.' or w=='-' or w=='_':
            continue
        else:
            answer = answer.replace(w,'')
    #3단계: 연속되는 마침표 제거
    while True:
        if '..' not in answer:
            break
        else:
            answer = answer.replace('..','.')
    
    
    #4단계 : 마침표 처음과 끝일 때 예외처리
    if answer[0] == '.':
        answer = answer[1:]

    #5단계 : 빈문자열인 경우
    if len(answer)==0:
        answer ='aaa'
    
    if answer[-1] == '.':
        answer = answer[:-1]

    #6단계: 16자 이상인 경우
    if len(answer) > 15:
        answer = answer[0:15]
        if answer[-1] == '.':
            answer = answer[0:-1]
    #7단계 : 2자 이하인 경우
    if len(answer) <=2 :
        while True:
            if len(answer)==3:
                break
            answer += answer[-1]
    
    return answer

print(solution('...!@BaT#*..y.abcdefghijklm'))
print(solution('z-+.^.'))
print(solution('=.='))
print(solution('123_.def'))
print(solution('abdcedfghijklmn.p'))