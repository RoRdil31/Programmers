import re, copy
from itertools import permutations as perm
def calc(n1,op,n2):
    if op == '+' : return n1 + n2
    elif op == '-' : return n1 - n2
    elif op == '*' : return n1 * n2
    

def solution(expression):
    answer = 0
    e = re.findall(r'\d+|[^\w\d]', expression)
    e = [int(i) if idx%2==0 else i for idx,i in enumerate(e)]
    ops = {i for i in e[1::2]}
    
    for op in perm(ops):
        lst = copy.deepcopy(e); print(op)
        for i in op: # * - +
            while i in lst:
                idx = lst.index(i)
                n1, _, n2 = lst.pop(idx-1),lst.pop(idx-1), lst.pop(idx-1)
                lst.insert(idx-1, calc(n1,i,n2))
                
        if abs(lst[0]) > answer : answer = abs(lst[0])
    
    return answer