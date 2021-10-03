import heapq

def solution(operations):
    heap_min = []
    heap_max = []
    
    for oper in operations:
        op, data = oper.split()
        if op == 'I':
            heapq.heappush(heap_min, int(data))
            heapq.heappush(heap_max, -int(data))
        if op == 'D':
            if len(heap_min) > 0 and len(heap_max) > 0:
                if data == '1':
                    heap_min.remove(-heapq.heappop(heap_max))
                else:
                    heap_max.remove(-heapq.heappop(heap_min))

    if len(heap_min)==0:
        return [0,0]
            
    return [-heap_max[0], heap_min[0]]