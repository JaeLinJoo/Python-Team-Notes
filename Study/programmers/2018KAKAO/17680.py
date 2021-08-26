#[1차] 캐시

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities)*5

    cache = []
    answer = 0

    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.append(cache.pop(cache.index(city)))
        else:
            answer+=5
            cache.append(city)
            if len(cache) > cacheSize:
                cache.pop(0)
    
    return answer

## 1, 5라고 하는 것보다 cache_hit, cache_miss로 명명하면 리얼 코드에서는 코드파악이 더 쉬울 것 같음

cacheSize = 5
cities =	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
print(solution(cacheSize,cities))


### 다른 사람 풀이 => 배울점 : deque의 maxlen을 이용!!
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time
