#부분 문자열
import sys

def find(S,T):
    pre = -1
    for s in S:
        idx = T.find(s,pre+1)
        if idx > -1 and pre < idx:
            pre = idx
        else:
            pre = -2
            break
    return pre

while True:
    testcase = sys.stdin.readline().strip()
    if not testcase:
        break

    S, T = testcase.split()
    pre = find(S,T)
    if pre >= 0:
        print('Yes')
    else:
        print('No')

