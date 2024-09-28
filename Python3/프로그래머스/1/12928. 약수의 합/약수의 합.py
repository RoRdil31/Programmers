# import math
# def solution(n):
#     sum=0
#     for i in range(1,n+1):
#         sum += i if n%i == 0 else 0
#     return sum

def solution(n):
    return sum([i for i in range(1,n+1) if n%i ==0])

# import math
# def solution(n):
#     sum=0
#     for i in range(1,math.ceil(math.sqrt(n))):
#         sum += (i+n//i)if n%i == 0 else 0
#     return sum