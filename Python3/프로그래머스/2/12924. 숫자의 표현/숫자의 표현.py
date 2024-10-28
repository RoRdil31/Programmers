def solution(num):
    cnt = 0
    for i in range(1,num//2+1):
        total = 0
        for j in range(i,num):
            total += j
            if total == num : cnt += 1; break
            if total > num : break
            
    return cnt + 1
    # return len([i for i in range(1,num+1,2) if num % i == 0])