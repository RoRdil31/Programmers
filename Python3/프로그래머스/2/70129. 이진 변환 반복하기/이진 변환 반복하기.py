def solution(s):
    cnt, zero = 0, 0
    while s != '1' :
        zero += s.count('0')
        s = bin(s.count('1'))[2:]
        cnt+=1
    
    return [cnt, zero]
    
    
    
    
    
    
    
    
    
#     cnt = 0
#     removed_zero = 0
    
#     while int(s,2) != 1:
#         cnt += 1
#         removed_zero += s.count('0')
#         s = bin(s.count('1'))
        
#     return [cnt,removed_zero-cnt+1]