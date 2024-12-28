from collections import Counter
def solution(N, stages):
    ans = {i:0 for i in range(1,N+1)}
    counter = Counter(stages)
    l = len(stages)
    
    for i in sorted(counter):
        if i==N+1 : break
        ans[i] = counter[i] / l
        l -= counter[i]
    
    return sorted(ans, key = lambda x : ans[x], reverse=True)





















# def solution(N, stages):
#     odd = {}
#     l = len(stages)
    
#     for i in range(1,N+1):
#         if l != 0:
#             odd[i] = stages.count(i) / l
#             l -= stages.count(i)
#         else: odd[i] = 0
        
#     return sorted(odd, key = lambda x:-odd[x])