from collections import Counter
from itertools import chain
def solution(n, wires):
    
    def calc_total(total, i, visited): 
        for j in dic[i]:
            if j not in visited:
                visited.append(j)
                total = calc_total(total+1, j, visited)

        return total
    
    counter = Counter(list(chain(*wires)))
    counter = counter.most_common()
    root_len = counter[0][1]
    roots = [i for i,cnt in counter if root_len == cnt]
    dic = {i:[] for i in range(1,n+1)}
    for v1, v2 in wires: dic[v1].append(v2); dic[v2].append(v1)
    
    answer = 9999
    for root in range(1,n+1):
        for i in dic[root]:
            visited = [root, i]
            g1 = calc_total(1, i, visited)
            if abs(n - 2*g1) < answer : answer = abs(n - 2*g1)
    
    return answer

