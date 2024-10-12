def solution(n):
    prime_nums = set(range(2,n+1))
    
    for i in range(2, int(n**0.5)+1):
        if i in prime_nums:
            prime_nums -= set(range(i*2,n+1,i))
            
    return len(prime_nums)