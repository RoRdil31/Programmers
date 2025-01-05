from itertools import product
def solution(numbers, target):
    cnt = 0
    nums = [(-x,x) for x in numbers]
    for i in product(*nums):
        if sum(i) == target: cnt += 1
    
    return cnt


















# from itertools import product
# def solution(numbers, target):
#     l = [(x, -x) for x in numbers]
#     print(l)
#     s = list(map(sum, product(*l)))
#     print(s)
#     return s.count(target)
# # def solution(numbers, target):
# #     global answer
# #     answer = 0
# #     def dfs(i,total):
# #         global answer
# #         if (i==len(numbers)):
# #             if total==target:
# #                 answer+=1
# #             return
# #         dfs(i+1,total+numbers[i])    
# #         dfs(i+1,total-numbers[i])
# #         return
# #     dfs(0,0)
# #     return answer