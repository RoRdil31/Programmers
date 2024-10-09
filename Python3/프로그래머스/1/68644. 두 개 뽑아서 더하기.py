from itertools import combinations as comb
def solution(numbers):
    return sorted(set([sum(c) for c in comb(numbers,2)]))
