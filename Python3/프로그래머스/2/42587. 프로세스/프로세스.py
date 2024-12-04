from collections import deque
def solution(priorities, location):
    prior = [[idx,i] for idx, i in enumerate(priorities)]
    q = deque(prior)
    cnt = 0
    while q:
        now = q.popleft()
        if any(now[1] < queue[1] for queue in q): q.append(now)
        else : 
            if now[0] == location : return cnt + 1
            cnt += 1
    return cnt + 1