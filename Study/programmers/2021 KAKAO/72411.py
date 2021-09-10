# 메뉴 리뉴얼
#최소 2가지 이상 단품메뉴
# 최소 2명이상의 손님으로부터 주문된 단품메뉴 조합
# 오름차순

from itertools import combinations, count
from collections import Counter
def solution(orders, course):
    answer = []

    for c in course:
        combs = []
        for ord in orders:
            ord = sorted(ord)
            if len(ord)<c:
                continue
            else:
                combs.extend(list(combinations(ord,c)))
        if combs == []:
            continue
        combs = sorted(combs)
        counter = Counter(combs)
        order = counter.most_common()
        max_cnt = order[0][1]
        modes = []
        if max_cnt >= 2:
            for num in order:
                if num[1] == max_cnt:
                    modes.append(num[0])
        for m in modes:
            answer.append(''.join(m))
        
    answer =sorted(answer)
    print(answer)
    return answer

#solution(["ABD","AD","AB","ABC"],[2])
solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])
solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5])
solution(["XYZ", "XWY", "WXA"],[2,3,4])

