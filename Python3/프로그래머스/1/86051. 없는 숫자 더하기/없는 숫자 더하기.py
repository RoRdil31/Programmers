def solution(numbers):
    return 45-sum([i if i in [1,2,3,4,5,6,7,8,9,0] else 0 for i in numbers])