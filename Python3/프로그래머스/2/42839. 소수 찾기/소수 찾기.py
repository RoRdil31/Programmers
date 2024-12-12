from itertools import permutations
def solution(numbers):
    cnt = 0
    availables = set()
    # print(list(numbers))
    numbers = [i for i in numbers]
    
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            num = int(''.join(j))
            if num > 1 : availables.add(num)
            
    for i in availables:
        if not sum(1 for j in range(2, int(i**0.5)+1) if i%j==0) : cnt += 1
        
#     for i in range(len(numbers)):
#         availables |= set(map(int, map("".join, permutations(list(n), i + 1))))
#     a -= set(range(0, 2))
#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))
        
    return cnt
