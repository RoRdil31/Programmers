def solution(price, money, count):
    return max(sum(price*i for i in range(1,count+1))-money,0)
