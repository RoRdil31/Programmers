def solution(seq, k):
    total, limit_len, idx = 0, 0, -1
    if k in seq : return [seq.index(k), seq.index(k)]
    
    for i in range(len(seq)-1, -1, -1):
        total += seq[i]
        while total > k :
            total -= seq.pop()
            
        if total == k : 
            if limit_len and len(seq)-1-i > limit_len : return [idx, idx+limit_len]
            else : limit_len = len(seq) - 1 - i; idx = i
        
    return [idx, idx+limit_len]
