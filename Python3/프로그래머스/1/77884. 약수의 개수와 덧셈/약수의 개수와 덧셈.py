def solution(left, right):
    sign = []
    for n in range(left,right+1):
        cnt = 0
        for i in range(1, int(n**(1/2))+1):
            if n%i == 0 : 
                cnt += 1
                if i**2 != n: cnt += 1
        sign.append(1 if cnt%2==0 else -1)
    
    return sum([sign[i]*n for i,n in enumerate(range(left,right+1))])