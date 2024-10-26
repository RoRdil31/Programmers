from datetime import datetime
def solution(today, terms, privacies):
    answer = []
    term = {}
    today = datetime.strptime(today,'%Y.%m.%d')
    
    for i in terms:
        term[i[0]] = int(i[2:])
        
    for idx,i in enumerate(privacies):
        date, sort = datetime.strptime(i[:10],'%Y.%m.%d'), i[-1]
        diff = [(today.year-date.year)*12 + today.month-date.month, today.day - date.day]
        if diff[1] < 0 : # day 차이가 음수라면 1개월을 day로 전환.
            diff[0] -= 1
            diff[1] += 28
        if diff[0] >= term[sort]: 
            answer.append(idx+1)
        
    return answer