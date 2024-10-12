from itertools import combinations as comb
def solution(nums):
    answer = 0
    
    sums = [sum(c) for c in comb(nums,3)]
    
    for n in sums:
        if not sum(1 for i in range(2,int(n**0.5)+1) if n%i==0):
            answer += 1

    return answer