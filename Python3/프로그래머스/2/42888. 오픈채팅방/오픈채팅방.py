def solution(record):
    answer, result = {}, []
    for r in record:
        if r[0]=='C' or r[0]=='E':
            answer[r.split(' ')[1]] = r.split(' ')[2]
    
    for r in record:
        split_value = r.split(' ')
        state, user = split_value[0], split_value[1]
        
        if state.startswith('E') :
            result.append(f'{answer[user]}님이 들어왔습니다.')
        elif state.startswith('L') :
            result.append(f'{answer[user]}님이 나갔습니다.')
    
    return result