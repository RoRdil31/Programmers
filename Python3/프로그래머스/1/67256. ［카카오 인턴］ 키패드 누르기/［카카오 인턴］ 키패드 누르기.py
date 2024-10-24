import numpy as np
def solution(numbers, hand):
    result = ''
    l, r = [3,0], [3,2]
    phone = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    matrix = np.array(phone,dtype='object') # object를 해줘야 np.where에서 오류 안 남.
    
    for num in numbers:
        idxs = np.where(matrix == num) # 눌러야 할 숫자 위치 찾기.
        idx = [idxs[0][0], idxs[1][0]]
        
        if idx[1] == 0 : l = idx; result += 'L' # 왼손(147)
        elif idx[1] == 2 : r = idx; result += 'R' # 오른손(369)
        else : # 가운데 숫자 (2,5,8,0)
            if abs(l[0]-idx[0])+abs(l[1]-idx[1]) < abs(r[0]-idx[0])+abs(r[1]-idx[1]) : #왼손 가까움.
                l = idx
                result += 'L'
            elif abs(l[0]-idx[0])+abs(l[1]-idx[1]) > abs(r[0]-idx[0])+abs(r[1]-idx[1]) : #오른손 가까움.
                r = idx
                result += 'R'
            else : # 거리 같음.
                if hand == 'left' : l = idx; result += 'L'
                else : r = idx; result += 'R'
        
    
    return result