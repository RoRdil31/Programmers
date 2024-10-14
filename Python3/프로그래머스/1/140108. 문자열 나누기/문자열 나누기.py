def solution(s):
    cnt = 0
    while (s):
        x, not_x, idx = 1, 0, 0
        al = s[0]
        for i in range(1,len(s)):
            if s[i] == al : x+=1
            else : not_x += 1
            
            if x == not_x or i == len(s)-1: idx = i; break
        
        s = s[idx+1:]
        cnt += 1
    return cnt
