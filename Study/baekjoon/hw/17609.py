#회문
### ↓↓↓↓↓↓↓↓↓↓↓↓↓solution↓↓↓↓↓↓↓↓↓↓↓↓↓↓
def pseudo(x, left, right):
  while left < right:
    if x[left] == x[right]:
      left += 1
      right -= 1
    else:
      return False
  return True


def palindrome(x,left, right):
  while left < right:
    if x[left] == x[right]:
      left += 1
      right -= 1
    else:
      res1 = pseudo(x,left+1, right)
      res2 = pseudo(x,left,right-1)
      if res1 == True or res2 == True:
        return 1
      else:
        return 2
  return 0

t = int(input())
for i in range(t):
  x = input()
  res = palindrome(x,0,len(x)-1)
  print(res)

############시간초과############
# 회문
def palindrome(x):
  ps = False
  # 회문인 경우
  if x == x[::-1]:
    return 0
  # 유사회문의 경우
  else:
    for s in x:
      pseudo = x.replace(s,'')
      if pseudo == pseudo[::-1]:
        ps = True 
        continue
    if ps:
      return 1
    else:
      return 2

t = int(input())
res = []
for i in range(t):
  x = input()
  res.append(palindrome(x))

for r in res:
  print(r)
