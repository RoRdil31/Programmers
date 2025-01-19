from math import factorial as fact
def solution(n, k):
    answer = []
    p = list(range(1,n+1))
    
    k -= 1
    while p:
        f = fact(len(p)-1) # 2
        answer.append( p.pop( k//f ) ) # 2 (append(3))
        k = k%f
    
    return answer

# 4, 7, [2, 1, 3, 4]
















# import math
# def solution(n, k):
#     answer = []
#     p = [i for i in range(1,n+1)]
    
#     k -= 1
#     while p: 
#         fact = math.factorial(len(p)-1)
#         answer.append(p.pop( k//fact )) 
#         k %= fact
        
#     return answer

# # [1]
# # [1,2]             [2,1]
# # [1,2,3] [1,3,2]   [2,1,3] [2,3,1]   [3,1,2] [3,2,1]

# # n=4) (24) k=7                     k=6 [2,3,4]
# # [1,2,3,4] [1,2,4,3] [1,3,2,4] [1,3,4,2] [1,4,2,3] [1,4,3,2]
# # [2,1,3,4]