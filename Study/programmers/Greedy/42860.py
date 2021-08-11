#조이스틱
name = input()

def solution(name):
    answer = 0
    min_move = len(name)-1
    next = 0

    for n,s in enumerate(name):
        answer += min(ord(s)-ord('A'), ord('Z')-ord(s)+1)

        next = n+1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        min_move = min(min_move, n*2+len(name)-next)    
    
    answer += min_move

    return answer

print(solution(name))
