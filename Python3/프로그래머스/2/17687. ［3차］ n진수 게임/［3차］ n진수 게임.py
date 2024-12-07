def solution(n, t, m, p):
    answer,nums = '','0'
    for16 = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    for i in range(1,t*m):
        num = ''
        while i > 0:
            add = i%n
            if add >= 10 : add = for16[add]
            num += str(add)
            i = i//n
        nums += num[::-1]
    for i in range(p-1, len(nums), m):
        answer += nums[i]
    
    return answer[:t]
