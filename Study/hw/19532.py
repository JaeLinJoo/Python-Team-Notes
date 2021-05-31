#수학은 비대면강의입니다
def gcd(a,b):
  if a%b==0:
    return b
  else:
    return gcd(b, a%b)

a,b,c,d,e,f = map(int,input().split())

# a,d의 최소공배수
if a!=0 and b!=0:
  lcm = (a*d)/gcd(a,d)

  # lcm = m x a
  m = (lcm/a)
  # lcm = n x d
  n = (lcm/d)

  y = ((m*c-n*f)/(m*b-n*e))
  if a==0:
    x = ((f-e*y)/d)
  else:
    x = ((c-b*y)/a)

elif a==0 and b!=0:
  y = c/b
  x= ((f-e*y)/d)
elif d==0 and e!=0:
  y = f/e
  x = ((c-b*y)/a)

print(int(x),int(y))




