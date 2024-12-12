from itertools import permutations
def solution(numbers):
    cnt = 0
    availables = set()
    numbers = [i for i in numbers]
    
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            num = int(''.join(j))
            if num > 1 : availables.add(num)
            
    for i in availables:
        if not sum(1 for j in range(2, int(i**0.5)+1) if i%j==0) : cnt += 1
        
    return cnt
