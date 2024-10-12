def solution(num, limit, p):
    answer = 0
    for n in range(1,num+1):
        length =  sum(1 for i in range(1,int(n**0.5)+1) if n%i==0) * 2
        if n**0.5 == int(n**0.5) : length -= 1
        answer += p if length > limit else length
            
    return answer
