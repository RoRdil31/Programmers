# def solution(arr, divisor):
#     answer = sorted([i for i in arr if i%divisor == 0])
#     return answer if answer else [-1]

def solution(arr, divisor):
    return sorted([i for i in arr if i%divisor == 0]) or [-1]