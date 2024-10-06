from itertools import combinations as comb
def solution(number):
    
    return sum(not sum(c) for c in comb(number,3))