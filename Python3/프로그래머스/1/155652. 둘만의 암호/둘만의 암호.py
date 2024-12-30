def solution(s, skip, index):
    alpha = [i for i in 'abcdefghijklmnopqrstuvwxyz' if i not in skip]*5
    return ''.join([alpha[alpha.index(i) + index] for i in s])



















# def solution(s, skip, index): 
#     answer = ''
#     alpha = [i for i in 'abcdefghijklmnopqrstuvwxyz' if i not in skip]
#     for al in s:
#         answer += alpha[(alpha.index(al) + index) % len(alpha)]
    
#     return answer










# def solution(s, skip, index): # 'a' == 97, 'z' == 122
#     answer = ''
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     remaining = [i for i in alphabet if i not in skip]
    
#     for al in s:
#         if al in remaining:
#             idx = (remaining.index(al) + index) % len(remaining)
#             answer += remaining[idx]
            
#     return answer