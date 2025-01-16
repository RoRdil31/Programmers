def solution(n):
    ans = ''
    while n > 0:
        n -= 1
        n, r = n//3, n%3
        print(n, r)
        ans += str(r+1)
    
    return ans.replace('3','4')[::-1]
















# def solution(n):
#     answer = ''
#     while n > 0 :
#         n -= 1
#         answer += '124'[n%3]
#         n //= 3
    
#     return answer[::-1]
