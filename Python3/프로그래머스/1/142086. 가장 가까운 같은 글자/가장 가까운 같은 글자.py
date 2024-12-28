def solution(s):
    ans = []
    record = {}
    for idx,w in enumerate(s):
        if w in record.keys():
            ans.append(idx - record[w])
        else : ans.append(-1)
        record[w] = idx
        
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