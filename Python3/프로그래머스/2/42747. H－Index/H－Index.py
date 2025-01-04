def solution(citations):
    h = -1
    citations = sorted(citations, reverse=True)
    for i, c in enumerate(citations, start=1):
        if i >= c : h = max(i,c); break
    
    if h==-1 : return len(citations)
    return h + citations.count(h) - 1
            
    

# 6 5 3 / 1 0 => 3
# 6 5 3 3 / 0 => 
















# def solution(citations):
#     result = 0
#     citations.sort(reverse=True)
#     for idx, i in enumerate(citations, start = 1):
#         # cnt = sum(1 for j in citations if j >= i)
#         result = max(result, min(i, idx))
#     return result 
