#2021 KAKAO BLIND RECRUITMENT > 신규 아이디 추천

def solution(new_id):
    answer = ''
    answer = new_id.lower()
    
    for i in answer:
        if ord(i) >= ord('a') and ord(i)<=ord('z'):
            continue
        elif ord(i) >= ord('0') and ord(i)<=ord('9'):
            continue
        elif i == '-' or i == '_' or i == '.' :
            continue
        else:
            answer = answer.replace(i,'')
    
    while True:
        if '..' not in answer:
            break
        if '..' in answer:
            answer = answer.replace('..','.')

    if answer[0] == '.':
        answer = answer[1:]
    if len(answer) == 0:
        answer = 'aaa'
    if answer[-1] == '.':
        answer = answer[:-1]
    if len(answer)>=16:
        answer = answer[0:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    if len(answer)>0 and len(answer)<3:
        while True:
            if len(answer)==3:
                break
            answer += answer[-1]
        
    return answer

new_id = input()

print(solution(new_id))