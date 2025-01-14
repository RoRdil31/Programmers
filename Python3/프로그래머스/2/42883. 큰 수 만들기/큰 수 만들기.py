def solution(number, k):
    stack = []
    
    for i in number:
        while stack and stack[-1] < i and k > 0:
            stack.pop()
            k -= 1
        stack.append(i)
    if k > 0 : stack = stack[:-k]
    return ''.join(stack)




















# def solution(number, k):
#     stack = []
    
#     for i in number:
#         while stack and stack[-1] < i and k > 0:
#             stack.pop()
#             k -= 1
#         stack.append(i)
    
#     if k > 0 : stack = stack[:-k]
    
#     return ''.join(stack)

# # def solution(number, k):
# #     answer = ''
# #     max_v, max_index, a_len = number[0], 0, len(number)-k
    
# #     while a_len:
# #         if a_len == 1 : answer += max(number[max_index:]); return answer
    
# #         max_v = max(number[max_index: -a_len+1])
# #         max_index += number[max_index: -a_len+1].index(max_v)
        
# #         answer += max_v
# #         max_index += 1
# #         a_len -= 1
        
# #     return answer

# # 테스트 1 〉	통과 (0.01ms, 10.2MB)
# # 테스트 2 〉	통과 (0.02ms, 10.2MB)
# # 테스트 3 〉	통과 (0.03ms, 10.2MB)
# # 테스트 4 〉	통과 (0.80ms, 10.3MB)
# # 테스트 5 〉	통과 (1.04ms, 10.2MB)
# # 테스트 6 〉	통과 (145.62ms, 10.2MB)
# # 테스트 7 〉	통과 (284.97ms, 10.2MB)
# # 테스트 8 〉	통과 (2717.23ms, 10.5MB)
# # 테스트 9 〉	통과 (186.98ms, 11.5MB)
# # 테스트 10 〉	실패 (시간 초과)
# # 테스트 11 〉	통과 (0.00ms, 10.2MB)
# # 테스트 12 〉	통과 (0.01ms, 10.1MB)