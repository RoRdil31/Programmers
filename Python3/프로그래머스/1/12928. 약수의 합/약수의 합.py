def solution(n):
    a = [i for i in range(1, int(n**0.5)+1) if n//i == n/i]
    a.extend([n//i for i in a])
    return sum(set(a))













# import math
# def solution(n):
#     l1 = [i for i in range(1,int(math.sqrt(n))+1) if n%i == 0]
#     l1.extend([n//i for i in l1])
#     return sum(set(l1))