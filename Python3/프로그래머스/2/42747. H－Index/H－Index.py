def solution(citations):
    result = 0
    citations.sort(reverse=True)
    for idx, i in enumerate(citations, start = 1):
        # cnt = sum(1 for j in citations if j >= i)
        result = max(result, min(i, idx))
    return result 
    # answer = max(map(min, enumerate(citations, start=1)))
    # return answer
