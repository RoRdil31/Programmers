# Basic for문
def solution(n):
    sum=0
    for i in range(1,n+1):
        sum += i if n%i == 0 else 0
    return sum

# list comprehension
def solution(n):
    return sum([i for i in range(1,n+1) if n%i ==0])

# sqrt로 for문 연산 줄이는 방법
import math
def solution(n):
    l1 = [i for i in range(1,int(math.sqrt(n))+1) if n%i == 0]
    l1.extend([n//i for i in l1])
    return sum(set(l1))
