from collections import deque
def solution(people, limit):
    people = deque(sorted(people, reverse=True))
    cnt = 0
    while people:
        w = people.popleft()
        if people and (w + people[-1]) <= limit: people.pop()
        cnt += 1
    
    return cnt


















# def solution(people, limit):
#     cnt = 0
#     people = sorted(people,reverse=True)
    
#     for i in people:
#         total = i
#         if total + people[-1] <= limit : people.pop()
#         cnt += 1
            
#     return cnt
