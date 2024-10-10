def solution(k, m, score):
    price = 0
    score = sorted(score,reverse=True)
    
    for i in range(0,len(score)//m*m,m):
        price += m * min(score[i:i+m])
    
    return price



def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m
