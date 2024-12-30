from collections import Counter
def solution(X, Y):
    answer = ''
    counter = Counter(X) & Counter(Y)
    sorted_keys = sorted(counter.keys(), reverse=True)
    for i in sorted_keys: answer += i*counter[i]
    # answer = ''.join(sorted(counter.elements(), reverse=True))
    if answer != '' and answer.count('0') == len(answer) : return '0'
    
    return answer if answer else '-1'
















# from collections import Counter
# def solution(X, Y):
#     answer = ''
#     x = Counter(X)
#     y = Counter(Y)
    
#     for i in x :
#         if i in y :
#             answer += i*min(x[i],y[i])
#     if answer !='' and answer.count('0') == len(answer) : return '0'
#     return ''.join(sorted(answer,reverse=True)) if answer!='' else "-1"
