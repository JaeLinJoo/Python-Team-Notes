#[1차] 뉴스 클러스터링
str1 = input()
str2 = input()

import math

def solution(str1, str2):

    def preprocessing(str):
        str = str.upper()
        result = []
        for i in range(len(str)-1):
            if str[i:i+2].isalpha():
                    result.append(str[i:i+2])
            else:
                continue
        
        return result
    
    set_str1 = preprocessing(str1)
    set_str2 = preprocessing(str2)

    if len(set_str1)+len(set_str2)==0:
        return 65536

    s1_copy = set_str1.copy()
    s2_copy = set_str2.copy()
        
    inter = []
    for s1 in set_str1:
        if s1 in s2_copy:
            inter.append(s1)
            s1_copy.remove(s1)
            s2_copy.remove(s1)
    union = inter + s1_copy + s2_copy

    answer = math.trunc((len(inter)/(len(union))*65536))
    return answer

print(solution(str1,str2))

#### 다른 사람 풀이
def solution(str1, str2):

    list1 = [str1[n:n+2].lower() for n in range(len(str1)-1) if str1[n:n+2].isalpha()]
    list2 = [str2[n:n+2].lower() for n in range(len(str2)-1) if str2[n:n+2].isalpha()]

    tlist = set(list1) | set(list2)
    res1 = [] #합집합
    res2 = [] #교집합

    if tlist:
        for i in tlist:
            res1.extend([i]*max(list1.count(i), list2.count(i)))
            res2.extend([i]*min(list1.count(i), list2.count(i)))

        answer = int(len(res2)/len(res1)*65536)
        return answer

    else:
        return 65536