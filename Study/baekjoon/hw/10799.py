#쇠막대기
s = input()

stack = ['(']
cnt = 0
for i in range(1,len(s)):
    if s[i] == '(':
        stack.append(s[i])
    elif s[i] == ')' and s[i-1] == '(':
        stack.pop()
        cnt += len(stack)
    elif s[i] == ')':
        stack.pop()
        cnt += 1

print(cnt)