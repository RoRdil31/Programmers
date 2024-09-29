# def solution(n):
#     return list(reversed([int(i) for i in list(str(n))]))

def solution(n):
    return [int(i) for i in reversed(str(n))]
