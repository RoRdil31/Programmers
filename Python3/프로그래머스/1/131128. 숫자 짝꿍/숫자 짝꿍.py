from collections import Counter
def solution(X, Y):
    answer = ''
    a = Counter(X) & Counter(Y)
    if not a : return '-1'

    for v, cnt in sorted(a.items(), key=lambda x:-int(x[0])): answer += v*int(cnt)
    
    return answer if answer.count('0')!=len(answer) else '0'











# from collections import Counter
# def solution(X, Y):
#     answer = ''
#     counter = Counter(X) & Counter(Y)
#     for i in sorted(counter.keys(), reverse=True): answer += i*counter[i]
    
#     if answer != '' and answer.count('0') == len(answer) : return '0'
#     return answer if answer else '-1'













# # from collections import Counter
# # def solution(X, Y):
# #     answer = ''
# #     x = Counter(X)
# #     y = Counter(Y)
    
# #     for i in x :
# #         if i in y :
# #             answer += i*min(x[i],y[i])
# #     if answer !='' and answer.count('0') == len(answer) : return '0'
# #     return ''.join(sorted(answer,reverse=True)) if answer!='' else "-1"
