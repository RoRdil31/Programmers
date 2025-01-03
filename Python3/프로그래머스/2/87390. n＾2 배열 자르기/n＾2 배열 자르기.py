def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        answer.append(max(i//n+1, i%n+1))
        
    return answer

















# def solution(n, left, right):
#     result = []

#     for i in range(left, right+1):
#         y, x = i//n, i%n
#         value = max(y,x) + 1
#         result.append(value)

#     return result