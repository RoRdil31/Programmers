def solution(n,a,b):
    cnt = 0
    while a!=b :
        a, b = (a+1)//2, (b+1)//2
        cnt += 1
    
    return cnt


# 0 0 0 1 0 0 1 0
# 0 1 0 1
# 1 1













# def solution(n,a,b):
#     rnd = 0
#     while b!=a:
#         rnd += 1
#         a,b = (a+1)//2, (b+1)//2
    
#     return rnd
