def solution(N, stages):
    answer = []
    l = len(stages)
    for i in range(1,N+1):
        if i in stages:
            cnt = stages.count(i)
            answer.append((i,cnt/l))
            l -= cnt
        else : answer.append((i,0))
        
    return [i[0] for i in sorted(answer, key = lambda x : (-x[1],x))]





















# def solution(N, stages):
#     odd = {}
#     l = len(stages)
    
#     for i in range(1,N+1):
#         if l != 0:
#             odd[i] = stages.count(i) / l
#             l -= stages.count(i)
#         else: odd[i] = 0
        
#     return sorted(odd, key = lambda x:-odd[x])