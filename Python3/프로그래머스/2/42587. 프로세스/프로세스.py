from collections import deque
def solution(priorities, location):
    l = len(priorities)
    queue = deque([(i,p) for i,p in enumerate(priorities)])
    
    max_value = max(priorities)
    while queue:
        idx, p = queue.popleft()
        if p == max_value and idx == location: break
        elif p == max_value: priorities.remove(p); max_value = max(priorities)
        else : queue.append((idx,p))
        
    
    return l - len(queue)



















# from collections import deque
# def solution(priorities, location):
#     prior = [[idx,i] for idx, i in enumerate(priorities)]
#     q = deque(prior)
#     cnt = 0
#     while q:
#         now = q.popleft()
#         if any(now[1] < queue[1] for queue in q): q.append(now)
#         else : 
#             if now[0] == location : return cnt + 1
#             cnt += 1
#     return -1 # cnt + 1