from collections import deque
def solution(bridge_length, L, trucks):
    cnt, W = 0, 0
    bridge = deque([0]*bridge_length)
    
    for truck in trucks:
        W -= bridge.popleft()
        while W + truck > L:
            W -= bridge.popleft()
            bridge.append(0)
            cnt += 1
        bridge.append(truck)
        W += truck
        cnt += 1
        
    return cnt + bridge_length


# _7 7_ _4 45 5_ _6 6_ __
















# from collections import deque
# def solution(bridge_length, L, trucks):
    
#     q = deque()
#     cnt = 0

#     for i in range(bridge_length):
#         q.append(0)

    

#     length = len(trucks)
#     i=0
#     q_L = 0
    
#     while(i<length):
        
#         if q[0] != 0 : q_L -= q[0]
#         q.popleft()
        

#         # if sum(q)+trucks[i] <= L:
#         if q_L+trucks[i] <= L:
#             q.append(trucks[i])
#             q_L += trucks[i]
#             i+=1

#         else:
#             q.append(0)

#         cnt+=1


#     while(sum(q)):
#         q.popleft()
#         q.append(0)
#         cnt+=1


#     return cnt