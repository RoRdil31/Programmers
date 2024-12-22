from collections import Counter
from itertools import combinations as comb
def solution(orders, course):
    answer = []
    for cnt in course:
        comb_list = []
        for order in orders:
            comb_list.extend(comb(sorted(order), cnt))
            
        count = Counter(comb_list)
        if count :
            max_count = max(count.values())
            if max_count >= 2:
                for combo, freq in count.items():
                    if freq == max_count:
                        answer.append("".join(combo))
    
    
    return sorted(answer)