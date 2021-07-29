from itertools import combinations

def solution(orders, course):
    answer = []
    for c in course:
        combs = {}
        for o in orders:
            if len(o) < c :
                continue
            
            else :
                comb = list(combinations(o,c))
                
                for com in comb:
                    com = tuple(sorted(com))
                    if combs.get(com):
                        combs[com] += 1
                    else:
                        combs[com] = 1
        
        for k,v in combs.items():
            if max(combs.values()) < 2 :
                continue
            if max(combs.values()) == v:
                result = ''
                for i in k:
                    result += i
                answer.append(result) 

    answer.sort()      
    return answer

orders = list(map(str, input().split()))
course = list(map(int, input().split()))

print(solution(orders, course))