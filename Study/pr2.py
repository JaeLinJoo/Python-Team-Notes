# 윤년

x = int(input())

def check(x):
  if x%400 == 0:
    return 1
  if x%400 != 0 and x%100 == 0:
    return 0
  if x%4 == 0 and x%100 != 0 :
    return 1
  else :
    return 0
  
print(check(x))

  
  