def solution(n):
    n1, n2 = 0,1
    for i in range(n):
        n2, n1 = n1+n2, n2
    
    return n2 % 1000000007



















# from collections import deque
# def solution(n):
#     if n==1 : return 1
#     elif n==2 : return 2  
#     dp = deque([1,2])
    
#     for _ in range(3, n+1):
#         dp.append(dp.popleft() + dp[0])
    
#     return dp[-1] % 1000000007