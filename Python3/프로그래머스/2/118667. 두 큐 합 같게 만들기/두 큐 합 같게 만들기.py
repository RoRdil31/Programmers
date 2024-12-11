from collections import deque
def solution(queue1, queue2):
    cnt, q1, q2, origin_len = 0, deque(queue1), deque(queue2), len(queue1)
    sum1, sum2 = sum(q1), sum(q2)
    
    def popinsert(big, small, big_sum, small_sum):
        num = big.popleft()
        small.append(num)
        return big, small, big_sum-num, small_sum+num
    
    while 2 * (origin_len+2) > cnt :
        if sum1 == sum2 : return cnt
    
        if sum1 > sum2 : q1, q2, sum1, sum2 = popinsert(q1, q2, sum1, sum2)
        else : q2, q1, sum2, sum1 = popinsert(q2, q1, sum2, sum1)
        cnt += 1
    
    return -1

