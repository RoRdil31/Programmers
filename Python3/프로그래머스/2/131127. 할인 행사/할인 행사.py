from collections import Counter
def solution(want, number, discount):
    wants = {i:j for i,j in zip(want, number)}
    want_len = sum(number)
    cnt = 0
    
    for i in range(len(discount) - want_len+1):
        dis = Counter(discount[i:i+want_len])
        out = True
        for w in want: dis[w] -= wants[w]
        for v in dis.values():
            if v > 0 : out = False; break
        if out : cnt += 1
            
    return cnt
