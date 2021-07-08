#문자열 게임 2
def check(word, k):
    w_list = set(word)
    pos_w = []
    for w in w_list:
        if word.count(w) >= k :
            pos_w.append((w,word.count(w)))
    
    return pos_w

def find(word, k, pos_w):
    idx = [[] for _ in range(len(pos_w))]
    j = 0
    for w,cnt in pos_w:
        for i in range(cnt):
            idx[j].append(word.find(w))
            word = word.replace(w,'-',1)
        j += 1
    return idx
    
t = int(input())

for i in range(t):
    word = input()
    k = int(input())

    pos_w = check(word,k)
    
    if len(pos_w) == 0:
        print(-1)
    else:
        idx = find(word, k, pos_w)
        lenght = []
        for i in range(len(idx)):
            if len(idx[i]) == k:
                lenght.append(idx[i][k-1]-idx[i][0]+1)
            else:
                for j in range(len(idx[i])-k+1):
                    lenght.append(idx[i][len(idx[i])-1-j]-idx[i][len(idx[i])-k-j]+1)
        
        print(min(lenght), max(lenght))

