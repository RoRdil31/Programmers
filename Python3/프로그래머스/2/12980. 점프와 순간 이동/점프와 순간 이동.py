def solution(n):
    
#     answer = 0
#     while n>0 :
#         if n % 2 == 0: n = n//2; continue
#         else : n -= 1; answer += 1
    
#     return answer

    return bin(n).count('1')
    
    