def solution(n):
    
    before, after, total = 0, 1, 0
    for i in range(n-1):
        total = before + after
        before = after
        after = total
    
    return total % 1234567
     
    
    
    
    
    
    
    
    
    
#     first = 0
#     second = 1
    
#     for i in range(n-1):
#         third = first + second
#         first = second
#         second = third
        
    
    
    
    
#     return second % 1234567