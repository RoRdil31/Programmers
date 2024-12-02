def solution(citations):
    result = 0
    citations.sort(reverse=True)
    for i in citations:
        cnt = sum(1 for j in citations if j >= i)
        result = max(result, min(i, cnt))
        
    return result