def solution(b, y):
    
    ys = [i for i in range(1,y+1) if y%i == 0]
    for i in ys[::-1]:
        if b == (i+2 + y//i)*2 : return [i+2, y//i+2]
        
    
    
    
    
    
    
    
    
#     nums = [num for num in range(1,y+1) if y % num == 0]
#     nums = sorted(nums,reverse=True)
    
#     for i in range(len(nums)):
#         if b == ((nums[i]+2) + (nums[-1-i]))*2:
#             return [nums[i]+2, nums[-1-i]+2]
    
#     return -1