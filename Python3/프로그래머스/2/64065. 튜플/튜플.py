import re
from collections import Counter
def solution(s):
    s = Counter(re.findall('\d+', s))
    # for v, cnt in s.most_common() : answer.append(int(v))
    
    return [int(v) for v, cnt in s.most_common()]
    
#     answer, lst = [], []
#     for i in s[2:-2].split('},{'): lst.append(i.split(','))
#     sorted_s = sorted(lst, key = lambda x : len(x))

#     answer.append(sorted_s[0][0])
#     for sub in sorted_s[1:] :
#         print(set(sub) - set(answer))
#         rest = (set(sub) - set(answer))
#         r = (list(rest)[0])
#         answer.append(r)
        
#     return [int(i) for i in answer]