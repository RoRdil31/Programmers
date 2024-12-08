def solution(left, right):
    return sum(-n if int(n**0.5)==(n**0.5) else n for n in range(left,right+1))























# # def solution(left, right):
# #     sign = []
# #     for n in range(left,right+1):
# #         cnt = 0
# #         for i in range(1, int(n**(1/2))+1):
# #             if n%i == 0 : 
# #                 cnt += 1
# #                 if i**2 != n: cnt += 1
# #         sign.append(1 if cnt%2==0 else -1)
    
# #     return sum([sign[i]*n for i,n in enumerate(range(left,right+1))])


# # def solution(left, right):
# #     answer = 0
# #     for i in range(left,right+1):
# #         if int(i**0.5)==i**0.5:
# #             answer -= i
# #         else:
# #             answer += i
# #     return answer


# # def solution(left, right):
# #     return sum(n if (n ** 0.5) % 1 else -n for n in range(left, right + 1))

# def solution(left, right):
#     return sum(-n if int(n**0.5)==(n**0.5) else n for n in range(left, right + 1))