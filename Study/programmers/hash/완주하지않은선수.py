from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]

"""
#Counter
- 항목의 개수를 셀때 사용
    ㄴ 리스트나 셋을 인자로 넘기면 각 항목을 키로 해서 개수를 알려준다
"""