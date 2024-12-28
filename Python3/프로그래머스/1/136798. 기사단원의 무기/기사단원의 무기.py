def solution(number, limit, power):
    nums = []
    for i in range(1,number+1):
        cnt = sum(1 for j in range(1,int(i**0.5)+1) if i%j==0)*2
        if int(i**0.5) == (i**0.5) : cnt -= 1
        if cnt > limit: cnt = power
        nums.append(cnt)
    
    return sum(nums)


















# def solution(num, limit, p):
#     answer = 0
#     for n in range(1,num+1):
#         length =  sum(1 for i in range(1,int(n**0.5)+1) if n%i==0) * 2
#         if n**0.5 == int(n**0.5) : length -= 1
#         answer += p if length > limit else length
            
#     return answer
