from collections import deque
def solution(cacheSize, cities):
    if (cacheSize == 0) : return 5*len(cities)
    cnt, cache = 0, []
    q = deque(maxlen = cacheSize)
    cities = [i.lower() for i in cities]
    
    for city in cities :
        if city in q :
            q.remove(city)
            q.append(city)
            cnt += 1
        else :
            q.append(city)
            cnt += 5
    return cnt

    # for city in cities:
    #     if city in cache : 
    #         cache.pop(cache.index(city))
    #         cache.insert(0, city)
    #         cnt += 1
    #     else :
    #         if len(cache) == cacheSize : cache.pop()
    #         cache.insert(0, city)
    #         cnt += 5
    # return cnt