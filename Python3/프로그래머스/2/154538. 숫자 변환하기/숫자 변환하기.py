from collections import deque
def solution(x, y, n):
    answer, queue = 0, deque()
    queue.append([y,0])
    
    while queue:
        y, cnt = queue.popleft()
        if x == y : return cnt
        elif x > y : continue
        
        if y%3 == 0 : queue.append([y//3, cnt+1])
        if y%2 == 0 : queue.append([y//2, cnt+1])
        queue.append([y-n, cnt+1])
    
    return -1
    
#     while queue:
#         x, cnt = queue.popleft()
#         if x == y : return cnt
#         elif x > y : continue
        
#         queue.append([x*3, cnt+1])
#         queue.append([x*2, cnt+1])
#         queue.append([x+n, cnt+1])
#     return -1


# x += n
# x *= 2
# x *= 3