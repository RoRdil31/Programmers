from collections import Counter
from itertools import combinations as comb
def solution(orders, course):
    result = []

    for cnt in course:
        comb_list = []
        for order in orders:
            comb_list += comb(sorted(order), cnt)
        
        most_ordered = Counter(comb_list).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]
    
    return [ ''.join(v) for v in sorted(result) ]
