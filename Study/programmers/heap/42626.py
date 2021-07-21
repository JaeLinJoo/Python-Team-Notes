#더 맵게

import heapq

def solution(scoville, K):
    heap = []
    for i in scoville:
        heapq.heappush(heap,i)
    answer = 0
    while heap[0]<K:
        try:
            new = heapq.heappop(heap) + heapq.heappop(heap)*2
            answer += 1
            heapq.heappush(heap, new)
        except IndexError:
            return -1
    return answer

scoville = list(map(int, input().split()))
k = int(input())

print(solution(scoville,k))
