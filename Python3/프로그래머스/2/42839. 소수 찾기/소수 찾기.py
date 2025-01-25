from itertools import permutations as perm
def solution(numbers):
    answer, nums = 0, set()
    for i in range(1,len(numbers)+1):
        for j in map(''.join, perm(numbers, i)):
            nums.add(int(j))
    nums -= {0,1}
    for num in nums:
        if sum(1 for i in range(2, int(num**0.5)+1) if num%i==0) == 0: answer += 1
        
    return answer



















# from itertools import permutations as perm
# def solution(numbers):
#     answer, nums = 0, set()
    
#     for i in range(1, len(numbers)+1):
#         nums |= set(map(int, map("".join, perm(list(numbers),i))))
#     nums -= {0,1}
#     for num in nums:
#         if not sum(1 for i in range(2, int(num**0.5)+1) if num%i == 0): answer += 1
    
#     return answer




















# from itertools import permutations as perm
# def solution(numbers):
#     prime, cnt = [], 0
#     for i in range(1, len(numbers)+1):
#         for j in perm(numbers, i):
#             prime.append(int(''.join(j)))
            
#     for num in set(prime):
#         if num == 0 or num == 1: continue
#         # if not sum(1 for j in range(2,int(num**0.5)+1) if num%j==0) : cnt += 1
#         for i in range(2, int(num**0.5)+1):
#             if num%i ==0: cnt -= 1; break
#         cnt += 1
        
#     return cnt













# # from itertools import permutations
# # def solution(numbers):
# #     cnt = 0
# #     availables = set()
        
# #     for i in range(len(numbers)):
# #         availables |= set(map(int, map("".join, permutations(list(numbers), i + 1))))
        
# #     availables -= set(range(0, 2))
# #     for i in availables:
# #         if not sum(1 for j in range(2,int(i**0.5)+1) if i%j==0) : cnt += 1
        
# #     return cnt