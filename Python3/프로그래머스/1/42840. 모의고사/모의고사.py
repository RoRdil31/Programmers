def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    s1 = sum(1 for idx,i in enumerate(answers) if p1[idx%len(p1)]==i)
    s2 = sum(1 for idx,i in enumerate(answers) if p2[idx%len(p2)]==i)
    s3 = sum(1 for idx,i in enumerate(answers) if p3[idx%len(p3)]==i)
    max_num = max(s1, s2, s3)
    
    return [idx+1 for idx,i in enumerate([s1,s2,s3]) if i==max_num]

















# def solution(answers):
#     persons = [[1, 2, 3, 4, 5],[2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
#     scores = []
#     for p in persons : 
#         cnt = 0
#         for idx, i in enumerate(answers):
#             if p[idx%len(p)]==i : cnt += 1
#         scores.append(cnt)
    
#     return [idx+1 for idx,s in enumerate(scores) if s==max(scores)]


