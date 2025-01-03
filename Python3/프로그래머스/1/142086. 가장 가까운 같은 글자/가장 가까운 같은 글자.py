def solution(s):
    ans = []
    d = {i:-1 for i in set(s)}
    
    for idx, i in enumerate(s):
        if d[i] == -1 : ans.append(d[i])
        else : ans.append(idx - d[i])
        d[i] = idx
        
    return ans

















# def solution(s):
#     answer = []
#     record = {}
#     for idx, c in enumerate(s):
#         if c in record:
#             answer.append(idx - record[c])
#         else :
#             answer.append(-1)
#         record[c] = idx
            
#     return answer


# record = {}
#     for idx,w in enumerate(s):
#         if w in record: ans.append(idx - record[w])
#         else : ans.append(-1)
#         record[w] = idx
        