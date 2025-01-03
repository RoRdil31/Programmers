def solution(elements):
    answer = []
    e = elements*2
    for i in range(1,len(elements)+1):
        for j in range(len(elements)):
            answer.append(sum(e[j:j+i]))
    
    return len(set(answer))




















# def solution(elements):
#     answer = []
#     circle = elements*2
#     for i,num in enumerate(elements):
#         answer.append(num)
#         for num2 in circle[i+1:i+len(elements)]:
#             num += num2
#             answer.append(num)
            
#     return len(set(answer))
    