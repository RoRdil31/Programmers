def solution(n):
    
    for n2 in range(n+1,1000001):
        if bin(n).count('1') == bin(n2).count('1') : return n2
    