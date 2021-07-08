# 기적의 매매법

# 현금
cash = int(input())

# 주가 정보
info = list(map(int,input().split()))

### 준현 BNP
j = 0 #준현이 보유한 주식
j_cash = cash #준현의 현금
for i in range(14):
  x = j_cash // info[i]
  j += x
  j_cash -= x*info[i]

# 준현 최종 보유 금액
fin_j = j_cash + (j * info[13])

### 성민 TIMING
s = 0 #성민 보유 주식
s_cash = cash # 성민 현금
for i in range(2,13):
  if info[i-2]>info[i-1] and info[i-1]>info[i]:
    x = s_cash//info[i+1]
    s += x
    s_cash -= x*info[i+1]
  if info[i-2]<info[i-1] and info[i-1]<info[i]:
    s_cash += s*info[i+1]
    s = 0

# 성민 최종 보유 금액
fin_s = s_cash + (s * info[13])

if fin_j>fin_s:
  print('BNP')
elif fin_j<fin_s:
  print('TIMING')
else:
  print('SAMESAME')


