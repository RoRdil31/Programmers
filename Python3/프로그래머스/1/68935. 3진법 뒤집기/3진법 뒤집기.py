def solution(n):
    ans = ''
    while n>0:
        ans += str(n%3)
        n //= 3
    
    return int(ans,3)






















# def solution(n):
#     ternary = ''
#     while n > 0:
#         ternary += str(n%3)
#         n = n//3
    
#     # up = len(ternary)-1
#     # for i in ternary:
#     #     answer += int(i)*(3**up)
#     #     up -= 1
        
#     return int(ternary,3)