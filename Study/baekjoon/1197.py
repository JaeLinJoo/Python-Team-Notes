#최소 스패닝 트리

def find_parent(parent, x):
    if parent[x]!=x:
        return find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

v,e =map(int,input().split())
parent = [i for i in range(v+1)]

edges = []
answer = 0

for _ in range(e):
    a,b,c = map(int, input().split())
    edges.append((c,a,b))

edges.sort()

for edge in edges:
    c,a,b =edge
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        answer += c

print(answer)

