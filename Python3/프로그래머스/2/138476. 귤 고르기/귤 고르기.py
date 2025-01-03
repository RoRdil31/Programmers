from collections import Counter
def solution(k, tangerine):
    cnt = 0
    counter = Counter(tangerine)
    
    for _, i in counter.most_common():
        k -= i
        cnt += 1
        if k <= 0 : return cnt
    

















# from collections import Counter
# def solution(k, tangerine):
#     cnt = 0
#     a = Counter(tangerine)
    
#     for item, count in a.most_common():
#         k -= count
#         cnt += 1
#         if k <= 0 : break
    
    
#     return cnt