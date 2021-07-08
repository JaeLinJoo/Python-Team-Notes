# 8진수 2진수
import math

x = input()

res = ''
for i in range(len(x)):
  if x[i] == '0':
    res += '000'
  elif x[i] == '1':
    res += '001'
  elif x[i] == '2':
    res += '010'
  elif x[i] == '3':
    res += '011'
  elif x[i] == '4':
    res += '100'
  elif x[i] == '5':
    res += '101'
  elif x[i] == '6':
    res += '110'
  else:
    res += '111'

if res[0:2]=='00':
  print(res[2::])
elif res[0]=='0':
  print(res[1::])
else:
  print(res)


