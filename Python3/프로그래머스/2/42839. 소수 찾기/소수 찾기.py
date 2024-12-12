from itertools import permutations
def solution(numbers):
    cnt = 0
    availables = set()
        
    for i in range(len(numbers)):
        availables |= set(map(int, map("".join, permutations(list(numbers), i + 1))))
        
    availables -= set(range(0, 2))
    for i in availables:
        if not sum(1 for j in range(2,int(i**0.5)+1) if i%j==0) : cnt += 1
        
    return cnt
