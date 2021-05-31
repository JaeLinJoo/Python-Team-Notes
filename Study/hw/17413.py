# 단어 뒤집기2

def rev_word(s):
  a = list(s.split())
  res =''
  for i in range(len(a)):
    if i==0:
      res = a[i][::-1]
    else:
      res += ' '+a[i][::-1]  
  return res

s = input()

val = s.find('<')
#'<' , '>' 를 포함하지 않은 경우
if val == -1:
  print(rev_word(s))

#태그를 포함한 경우
else:
  open = [0]
  close = [-1]
  result = []
  for i in range(len(s)):
    if s[i]=='<':
      result.append(rev_word(s[close[-1]+1:i]))
      open.append(i)
    if s[i]=='>':
      result.append(s[open[-1]:i+1])
      close.append(i)

  result.append(rev_word(s[close[-1]+1:]))

  #최종 출력
  for w in result:
    print(w,end='')
