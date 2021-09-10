#순위 검색

# 효율성 0점
def solution(info, query):
    info_list = [i.split(" ") for i in info]
    query_list = []
    for q in query:
        mid_q =q.split(" and ")
        fin_q = mid_q[0:3]+mid_q[3].split(" ")
        query_list.append(fin_q)
    
    answer = []
        
    for q in query_list:
        cnt = 0
        for i in info_list:
            check_count = 0 #5가 되면 모든 조건 충족됨을 나타낸다.
            for n in range(5):
                if q[n] == '-':
                    check_count+=1
                elif n==4 and int(q[n])<=int(i[n]):
                    check_count +=1
                elif q[n] == i[n]:
                    check_count +=1

            if check_count == 5:
                cnt+=1
        answer.append(cnt)    
    
        
    return answer

def solution(info, query):
    answer = []
    for que in query:
        q = que.split() #[언어,and,직군,and,경력,and,소울,점수]
        cnt = 0
        for inf in info:
            i = inf.split()
            if q[0] != '-' and q[0] != i[0]:
                continue
            if q[2] != '-' and q[2] != i[1]:
                continue
            if q[4] != '-' and q[4] != i[2]:
                continue
            if q[6] != '-' and q[6] != i[3]:
                continue
            if int(q[7]) <= int(i[4]):
                cnt += 1
        answer.append(cnt)
        
    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])


#### solution = 조합, 이진탐색
# 참고 : https://dev-note-97.tistory.com/131
from itertools import combinations
def solution(info, query):
    answer = []
    db = {}
    for i in info:                   # info에 대해 반복
        temp = i.split()
        conditions = temp[:-1]       # 조건들만 모으고, 점수 따로
        score = int(temp[-1])  
        for n in range(5):           # 조건들에 대해 조합을 이용해서  
            combi = list(combinations(range(4), n))
            for c in combi:
                t_c = conditions.copy()
                for v in c:          # '-'를 포함한 새로운 조건을 만들어냄.
                    t_c[v] = '-'
                changed_t_c = '/'.join(t_c)
                if changed_t_c in db:     # 모든 조건의 경우에 수에 대해 딕셔너리
                    db[changed_t_c].append(score)
                else:
                    db[changed_t_c] = [score]

    for value in db.values():             # 딕셔너리 내 모든 값 정렬
        value.sort()
 
    for q in query:                       # query의 모든 조건에 대해서
        qry = [i for i in q.split() if i != 'and']
        qry_cnd = '/'.join(qry[:-1])
        qry_score = int(qry[-1])
        if qry_cnd in db:                 # 딕셔너리 내에 값이 존재한다면,
            data = db[qry_cnd]
            if len(data) > 0:          
                start, end = 0, len(data)     # lower bound 알고리즘 통해 인덱스 찾고,
                while start != end and start != len(data):
                    if data[(start + end) // 2] >= qry_score:
                        end = (start + end) // 2
                    else:
                        start = (start + end) // 2 + 1
                answer.append(len(data) - start)      # 해당 인덱스부터 끝까지의 갯수가 정답
        else:
            answer.append(0)

    return answer

# 더 가독성이 좋은
def solution(info, query):
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))

    for k in data:
        data[k].sort()
    answer = list()
    for q in query:
        q = q.split()

        pool = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])
        l = 0
        r = len(pool)
        mid = 0
        while l < r:
            mid = (r+l)//2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid+1
            
        answer.append(len(pool)-l)

    return answer