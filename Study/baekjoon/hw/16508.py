##### ↓↓↓↓↓↓↓↓↓↓↓↓solution↓↓↓↓↓↓↓↓↓↓↓↓↓↓
from itertools import combinations

t = input()
n = int(input())
books = []
for _ in range(n):
    a, b = input().split()
    books.append((int(a), b))


def is_possible(books):
    # 책들의 문자 카운트를 저장해놓음
    d = {}
    for _, b in books:
        for ch in b:
            d[ch] = d.get(ch, 0)+1
            
    cnt = 0
    for ch in t:
        if d.get(ch, 0) > 0:
            cnt += 1
            d[ch] -= 1
    return cnt == len(t)

res = 1e9
for i in range(1, n+1):
    comb = combinations(books, i)
    for c in comb:
        if is_possible(c):
            tmp = sum([p for p, _ in c])
            res = min(res, tmp)
            
if res == 1e9:
    print(-1)
else:
    print(res)

####### ↓↓↓↓↓↓↓↓↓틀림, 이유 못찾음..↓↓↓↓↓↓↓↓↓↓
# 전공책
from collections import deque
import sys

def make_word(word, books):
    books.sort() #가격순으로 정렬
    bag = []
    queue = deque(list(word))
    print(queue)
    while queue:
        w = queue.popleft()
        for i in range(len(books)):
            if books[i][1].find(w)>-1:
                books[i][1]=books[i][1].replace(w,'',1)
                bag.append((i,w))
    print("bag: ",bag)
    bag.sort(key = lambda b : b[1])
    print("sorted bag: ", bag)
    count = [0]*len(books)
    for b in bag:
        count[b[0]] += 1
    print("count: ", count)
    max_index = count.index(max(count)) #가장 단어를 많이 포함하고 있는 책 인덱스
    print("max index: ", max_index)
    if max(count) == len(word):
        return books[max_index][0]
    else:
        pick = set() #단어 오려낼 책 index 저장
        length = len(word) #단어 만들 수 있는지 판단 여부
        total_price = 0
        for w in word:
            check = (max_index,w)
            if check in bag :
                pick.add(max_index)
                rem = bag.pop(bag.index(check))
                print("max index랑 같을 때 remove: ",rem)
                length -= 1
            else:
                for b in bag:
                    if b[1] == w:
                        pick.add(b[0])
                        rem = bag.pop(bag.index(b))
                        print("max index랑 다를 때 remove: ",rem)
                        length -= 1
                        break
        if length == 0:
            for p in pick :
                price = books[p][0]
                total_price += price
            return total_price
        else:
            return -1
    #fin_price = 0
    #for num in bag:
     #   fin_price += books[num][0]
    #return fin_price

t = sys.stdin.readline().rstrip() #단어
n = int(input()) #전공책 수
books = []
for i in range(n):
    price, title = input().split()
    books.append([int(price), title])

res = make_word(t, books)
print(res)