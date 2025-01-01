def solution(numbers, hand):
    answer = ''
    position = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2], '*':[3,0], 0:[3,1], '#':[3,2]}
    lh = position['*']
    rh = position['#']
    
    for i in numbers:
        if i in [1,4,7]: answer += 'L'; lh = position[i]
        elif i in [3,6,9]: answer += 'R'; rh = position[i]
        else: 
            len_left = (abs(lh[0]-position[i][0])+abs(lh[1]-position[i][1]))
            len_right = (abs(rh[0]-position[i][0])+abs(rh[1]-position[i][1]))

            if len_left < len_right: answer += 'L'; lh = position[i]
            elif len_left > len_right: answer += 'R'; rh = position[i]
            else: 
                if hand=='left': answer += 'L'; lh = position[i] 
                else: answer += 'R'; rh = position[i]
    
    return answer

















# import numpy as np
# def solution(numbers, hand):
#     result = ''
#     l, r = [3,0], [3,2]
#     phone = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
#     matrix = np.array(phone,dtype='object') # object를 해줘야 np.where에서 오류 안 남.
    
#     for num in numbers:
#         idxs = np.where(matrix == num) # 눌러야 할 숫자 위치 찾기.
#         idx = [idxs[0][0], idxs[1][0]]
        
#         if idx[1] == 0 : l = idx; result += 'L' # 왼손(147)
#         elif idx[1] == 2 : r = idx; result += 'R' # 오른손(369)
#         else : # 가운데 숫자 (2,5,8,0)
#             if abs(l[0]-idx[0])+abs(l[1]-idx[1]) < abs(r[0]-idx[0])+abs(r[1]-idx[1]) : #왼손 가까움.
#                 l = idx
#                 result += 'L'
#             elif abs(l[0]-idx[0])+abs(l[1]-idx[1]) > abs(r[0]-idx[0])+abs(r[1]-idx[1]) : #오른손 가까움.
#                 r = idx
#                 result += 'R'
#             else : # 거리 같음.
#                 if hand == 'left' : l = idx; result += 'L'
#                 else : r = idx; result += 'R'
        
    
#     return result