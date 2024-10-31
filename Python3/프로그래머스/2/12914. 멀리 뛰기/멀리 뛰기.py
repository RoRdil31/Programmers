import math
def solution(n): 
    answer = 0
    twos = n//2
    start = twos
    
    if n%2==1 : start += 1
    
    for i in range(start, n+1): 
        answer += math.comb(i,twos)
        twos -= 1
        
    return answer % 1234567
