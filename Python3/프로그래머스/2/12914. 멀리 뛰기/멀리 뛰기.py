import math
def solution(n):
    cnt = 0
    two, one = n//2, n%2
    while two >= 0:
        cnt += math.comb(two+one, one)
        two -= 1
        one += 2
    
    return cnt % 1234567

# 2 1, 1 2
# 111
















# import math
# def solution(n): 
#     answer = 0
#     twos = n//2
#     start = twos
    
#     if n%2==1 : start += 1
    
#     for i in range(start, n+1): 
#         answer += math.comb(i,twos)
#         twos -= 1
        
#     return answer % 1234567