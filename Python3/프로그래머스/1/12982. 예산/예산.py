# def solution(d, budget):
#     cnt = 0
#     for i in sorted(d):
#         if budget - i < 0 : return cnt
#         cnt += 1
#         budget -= i
    
#     return cnt

def solution(d, budget):
    
    d.sort()
    while budget < sum(d):
        d.pop()
    
    return len(d)