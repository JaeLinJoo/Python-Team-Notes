#위클리 챌린지 9주차

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    
    if parent[a]==parent[b]:
        return
    
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
    

def solution(n,wires):
    answer_list = []
    
    for i in range(len(wires)):
        parent = [i for i in range(n+1)]
        for j in range(len(wires)):
            if i == j: #wire 하나씩 제거하고 구해보기
                continue
            union_parent(parent,wires[j][0],wires[j][1])
    
        for k in range(1,n+1):
            find_parent(parent,k)

        cnt1 = parent.count(1)
        cnt2 = n-cnt1
        answer_list.append(abs(cnt1-cnt2))
    
    return min(answer_list)