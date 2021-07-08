#LSC
#### 부분수열 개념 공부.
first = input()
second = input()
len1 = len(first)
len2 = len(second)

LCS = [[0]*(len2+1) for _ in range(len1+1)]

for i in range(1,len1+1):
    for j in range(1,len2+1):
        if first[i-1] == second[j-1]:
            LCS[i][j] = LCS[i-1][j-1]+1
        else:
            LCS[i][j] = max(LCS[i][j-1], LCS[i-1][j])

print(LCS[-1][-1])