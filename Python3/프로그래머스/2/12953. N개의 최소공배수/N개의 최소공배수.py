import math
def solution(arr):
    
    while len(arr) >= 2:
        a, b = arr[0], arr[1]
        arr.append((a*b) // math.gcd(a,b))
        arr = arr[2:]
        
    return arr[0]
    
    
    
    
    
    
    
    
    
#     while (len(arr)>=2):
#         a = arr[0]
#         b = arr[1]
#         # while b : a,b = b, a%b
#         arr.append(abs(a*b)//math.gcd(a,b))
#         arr = arr[2:]
    
    
#     return arr[0]
