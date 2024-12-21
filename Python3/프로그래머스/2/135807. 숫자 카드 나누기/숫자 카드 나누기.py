from math import gcd
from functools import reduce
def solution(arrayA, arrayB):
    answer = []
    
    def check(gcd_value, array):
        for num in array:
            if num % gcd_value == 0 : return False
        return True
    
    gcd1 = reduce(gcd, arrayA)
    p1 = check(gcd1, arrayB)
    gcd2 = reduce(gcd, arrayB)
    p2 = check(gcd2, arrayA)
    
    if p1&p2 : return max(gcd1, gcd2)
    elif p1 : return gcd1
    elif p2 : return gcd2
    else : return 0
    
    return 0
