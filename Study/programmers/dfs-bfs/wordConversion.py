#단어 변환
begin = input()
target = input()
words = list(map(str, input().split()))

def compare(now, word):
    cnt = 0
    for n, w in zip(now, word):
        if n == w:
            cnt+=1
    if cnt == len(word)-1:
        return True
    else:
        return False

def solution(begin, target, words):
    if target not in words:
        return 0
    
    answer = 0
    visited = [False]*(len(words))
    stack = [begin]

    while stack:
        now = stack.pop()
        if now == target:
            return answer
        
        for i in range(len(words)):
            if not visited[i]:
                if compare(now, words[i]):
                    visited[i] = True
                    stack.append(words[i])
        answer += 1

print(solution(begin, target, words))