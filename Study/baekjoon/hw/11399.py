#ATM
n = int(input())
p = list(map(int, input().split()))

p.sort()
res = 0
for i in range(n):
    res += sum(p[0:i+1])

print(res)
