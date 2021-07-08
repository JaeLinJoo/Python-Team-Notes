#DNA
def hammming_dis(a,b):
  hd = 0 #해밍거리
  for i in range(len(a)):
    if a[i]!=b[i]:
      hd += 1
  return hd

def shortest_dna(n,m,data):
  dna = ''
  dic = ['A','C','G','T']
  for i in range(m):
    count = [0,0,0,0]
    for j in range(n):
      if data[j][i] == 'A':
        count[0] += 1
      elif data[j][i] == 'C':
        count[1] += 1
      elif data[j][i] == 'G':
        count[2] += 1
      else:
        count[3] += 1
    idx = count.index(max(count))
    dna += dic[idx]

  dis_sum = 0
  for i in range(n):
    dis_sum += hammming_dis(dna, data[i])
  
  return dna, dis_sum

n,m = map(int, input().split())

data = []
for i in range(n):
  data.append(input())

res_dna, res_sum = shortest_dna(n,m,data)

print(res_dna)
print(res_sum)