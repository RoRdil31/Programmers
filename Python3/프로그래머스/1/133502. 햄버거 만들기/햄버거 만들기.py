def solution(ingredient):
    cnt = 0
    stack = []
    for i in ingredient:
        stack.append(i)
        if len(stack)>=4 and stack[-4:]==[1,2,3,1]:
            stack.pop();stack.pop();stack.pop();stack.pop();
            cnt += 1
    
    return cnt


















# def solution(ingredient):
#     answer = 0
#     stack = []
    
#     for i in ingredient: # O(n)
#         stack.append(i) # O(1)
#         if stack[-4:] == [1,2,3,1] : answer += 1; del stack[-4:] # O(1)
    
#     return answer


# # Time Complexity : O(n^2)
# # hamberger = "1231"
# # str_ing = ''.join(map(str,ingredient))
# # while hamberger in str_ing :
# #         answer += 1
# #         str_ing = str_ing.replace(hamberger,'',1)