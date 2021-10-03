import heapq

def solution(jobs):
    answer = 0
    cnt, now = 0, 0
    start = -1 
    heap = []
    
    while cnt<len(jobs):
        for job in jobs:
            if start<job[0]<=now:
                heapq.heappush(heap, [job[1],job[0]])
        
        if len(heap)>0:
            req = heapq.heappop(heap)
            start = now
            now += req[0]
            answer += (now - req[1])
            cnt+=1
            
        else:
            now += 1
    
    return int(answer/len(jobs))