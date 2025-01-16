from collections import Counter
def solution(weights):
    answer = 0
    c = Counter(weights)
    for i in c.keys():
        if c[i] > 0:
            answer += (c[i] * (c[i]-1))/2 # 1:1
            answer += c[i] * c[i*2] # 1:2
            answer += c[i] * c[i*3/2] # 2:3
            answer += c[i] * c[i*4/3] # 3:4
    
    return answer




















# from collections import Counter
# def solution(weights):
#     answer = 0
#     counter = Counter(weights)
    
#     for i in range(100, 1001): # 1:1, 2:3, 2:4, 3:4 인 경우의 수.
#         if counter[i] > 0:
#             answer += (counter[i] * (counter[i]-1))/2 # 1:1 조합 nC2 = n(n-1)/2
#             answer += counter[i] * counter[i * 3 / 2] # 2:3
#             answer += counter[i] * counter[i * 2] # 2:4
#             answer += counter[i] * counter[i * 4 / 3] # 3:4
    
#     return answer