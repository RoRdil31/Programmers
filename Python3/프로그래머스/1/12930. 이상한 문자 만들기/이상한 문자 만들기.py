def solution(s):
    answer = []
    s = s.lower()
    for word in s.split(' '):
        ans = ''
        for idx,w in enumerate(word):
            if idx%2 == 0: ans += w.upper()
            else: ans += w
        answer.append(ans)
    return ' '.join(answer)






















# def solution(s):
#     result = []
#     for word in s.split(' '):
#         new_word = ''
#         for idx,w in enumerate(word):
#             if idx%2 ==0 : new_word += w.upper()
#             else : new_word += w.lower()
#         result.append(new_word)
#     return ' '.join(result)