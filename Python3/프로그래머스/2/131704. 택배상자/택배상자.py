from collections import deque
def solution(order):
    cnt, sub, con = 0, [''], deque([i for i in range(1,len(order)+1)])
    length = len(order)
    
    for box in order:
        i = length
        while i > 0:
            if con == deque([]) and sub[-1] != box : return cnt
            if (sub[-1]==box):
                sub.pop()
                cnt += 1
                break
            elif (con[0]==box):
                con.popleft()
                cnt += 1
                break
            else:
                sub.append(con.popleft())
                
            i -= 1
        
    return cnt
