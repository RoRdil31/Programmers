def solution(a, b, n):
    ans = 0
    while n >= a:
        ans += (n//a)*b
        n = (n//a)*b + n%a

    return ans

















# # def solution(a, b, n):
# #     answer = 0
# #     while n//a > 0 :
# #         answer += (n//a)*b
# #         n = (n//a)*b + n%a
        
# #     return answer
# solution = lambda a, b, n : max(n-b, 0) // (a-b)*b