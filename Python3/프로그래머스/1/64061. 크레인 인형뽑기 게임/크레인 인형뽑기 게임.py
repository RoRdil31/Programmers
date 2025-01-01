from collections import  deque
def solution(board, moves):
    cnt = 0
    board_t, stack = [], []
    
    for i in range(len(board[0])):
        lst = deque()
        for b in board:
            if b[i]!=0 : lst.append(b[i])
        board_t.append(lst)
        
    for m in moves:
        if board_t[m-1] : stack.append(board_t[m-1].popleft())
        if len(stack)>=2 and stack[-1]==stack[-2]: del stack[-2:]; cnt += 1
    
    return cnt * 2























# import numpy as np
# def solution(board, moves):
#     answer = 0
#     stack = []
#     board = np.array(board).T
#     board = (board).tolist()
#     board = [[i for i in row if i!=0] for row in board] # 0(인형없음) 제거.
    
#     for m in moves:
#         if board[m-1] : 
#             stack.append(board[m-1].pop(0)) # stack에 인형 넣고 board[m-1]에서 해당 인형 제거.
        
#         if len(stack)>=2 and stack[-1]==stack[-2] :
#             answer += 2
#             stack.pop()
#             stack.pop()
    
    
#     return answer