from itertools import product
def solution(word):
    answer = []
    fix = 'AEIOU'
    for i in range(1, len(fix)+1):
        for j in map(''.join, product(fix, repeat=i)):
            answer.append(j)
    
    return sorted(answer).index(word)+1


















# from itertools import product
# def solution(word):
#     l1 = []
#     words = ['A','E','I','O','U']
#     for i in range(1,6):
#         for j in list(product(words, repeat=i)):
#             l1.append(''.join(j))
#     print(l1)
#     l1.sort()
#     return l1.index(word)+1