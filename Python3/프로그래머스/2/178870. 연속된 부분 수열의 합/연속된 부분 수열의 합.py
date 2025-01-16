def solution(sequence, k):
    total,s1,s2 = 0,-1,len(sequence)-1
    answers = []
    
    for i in range(len(sequence)-1, -1, -1):
        v = sequence[i]
        if total + v >= k:
            if total + v == k: answers.append([i,s2])
            total = total - sequence[s2] + v
            s2 -= 1
        else: total += v
    
    final = 0
    min_diff = answers[0][1] - answers[0][0]
    for answer in answers:
        if answer[1]-answer[0] == min_diff : final = answer
        
    return final




















# def solution(seq, k):
#     total, limit_len, idx = 0, 0, -1
#     if k in seq : return [seq.index(k), seq.index(k)]
    
#     for i in range(len(seq)-1, -1, -1):
#         total += seq[i]
#         while total > k :
#             total -= seq.pop()
            
#         if total == k : 
#             if limit_len and len(seq)-1-i > limit_len : return [idx, idx+limit_len]
#             else : limit_len = len(seq) - 1 - i; idx = i
        
#     return [idx, idx+limit_len]
