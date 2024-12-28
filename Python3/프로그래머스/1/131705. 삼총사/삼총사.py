from itertools import combinations as comb
def solution(number):
    cnt = 0
    for c in comb(number,3):
        if sum(c) == 0: cnt += 1
    
    return cnt

















# from itertools import combinations as comb
# def solution(number):
#     return sum(not sum(c) for c in comb(number,3))
