from itertools import combinations as comb
from collections import Counter
def solution(orders, course):
    result = []
    for i in course:
        c = Counter()
        for order in orders: c += Counter(list(map(''.join, comb(sorted(order),i))))
        
        if c:
            max_cnt = c.most_common()[0][1]
            if max_cnt >= 2:
                for k,v in c.most_common():
                    if max_cnt != v : break
                    result.append(k)
            
    
    return sorted(result)