import math
def solution(n,m):
    gcd = math.gcd(n,m)
    
    return [gcd, n*m/gcd]
























# def solution(n, m):
    
#     gcd = 1
#     for i in range(min(n,m),0,-1):
#         if m%i == 0 and n%i == 0: 
#             gcd = i
#             break
    
#     return [gcd,(n*m)/gcd]