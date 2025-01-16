from math import gcd
from functools import reduce
def solution(A, B):
    answer = []
    def check(a, other):
        for i in other:
            if i%a == 0: return -1
        return a
    
    answer.append(check(reduce(gcd, A), B))
    answer.append(check(reduce(gcd, B), A))
    
    return max(answer) if max(answer)!=-1 else 0

















# from math import gcd
# from functools import reduce
# def solution(arrayA, arrayB):
#     answer = []
    
#     def check(gcd_value, array):
#         for num in array:
#             if num % gcd_value == 0 : return False
#         return True
    
#     gcd1 = reduce(gcd, arrayA)
#     p1 = check(gcd1, arrayB)
#     gcd2 = reduce(gcd, arrayB)
#     p2 = check(gcd2, arrayA)
    
#     if p1&p2 : return max(gcd1, gcd2)
#     elif p1 : return gcd1
#     elif p2 : return gcd2
#     else : return 0
    
#     return 0
