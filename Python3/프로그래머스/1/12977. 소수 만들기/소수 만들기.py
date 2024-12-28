from itertools import combinations as comb
def solution(nums):
    cnt = 0
    for i in comb(nums,3):
        if not sum(1 for j in range(2, int(sum(i)**0.5)+1) if sum(i)%j==0): cnt += 1
        
    return cnt



















# from itertools import combinations as comb
# def solution(nums):
#     answer = 0
    
#     sums = [sum(c) for c in comb(nums,3)]
    
#     for n in sums:
#         if not sum(1 for i in range(2,int(n**0.5)+1) if n%i==0):
#             answer += 1

#     return answer