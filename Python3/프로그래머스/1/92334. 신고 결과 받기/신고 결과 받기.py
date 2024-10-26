def solution(id_list, report, k):
    count = {}
    result = {}
    mail_count = {}
    for i in id_list:
        count[i] = 0
        result[i] = []
        mail_count[i] = 0
    
    for i in set(report):
        a, b = i.split(' ')
        count[b] += 1 # 신고된 횟수.
        result[b].append(a) # 신고한 사람들 저장.
    
    for i,item in count.items():
        if item >= k:
            for j in result[i]: mail_count[j] += 1
            
    return [i for i in mail_count.values()]