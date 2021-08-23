# 위클리 챌린지 4주차
## 직업군 추천하기


table = [input() for _ in range(5)]
languages = list(map(str, input().split()))
preference = list(map(int, input().split()))

def solution(table, languages, preference):
    table_dict = {}
    for t in table:
        s_list = t.split(" ")
        table_dict[s_list[0]] = s_list[1::]
    
    max_point = [-1, '']
    for job in table_dict:
        point = 0
        for i,lang in enumerate(languages):
            if lang in table_dict[job]:
                point += preference[i] * (5-table_dict[job].index(lang))
        if max_point[0] < point:
            max_point[0] = point
            max_point[1] = job
        elif max_point[0] == point:
            if max_point[1] > job:
                max_point[1] = job

    return max_point[1]

print(solution(table, languages, preference))

"""
SI JAVA JAVASCRIPT SQL PYTHON C#
CONTENTS JAVASCRIPT JAVA PYTHON SQL C++
HARDWARE C C++ PYTHON JAVA JAVASCRIPT
PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP
GAME C++ C# JAVASCRIPT C JAVA
PYTHON C++ SQL
7 5 5
"""

#다른 사람의 풀이
def solution(table, languages, preference):
    score = {}
    for t in table:
        for lang, pref in zip(languages, preference):
            if lang in t.split():
                score[t.split()[0]] = score.get(t.split()[0], 0) +  (6 - t.split().index(lang)) * pref
    return sorted(score.items(), key = lambda item: [-item[1], item[0]])[0][0]