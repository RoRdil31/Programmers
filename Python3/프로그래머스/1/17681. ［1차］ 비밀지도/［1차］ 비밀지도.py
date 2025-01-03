def solution(n, arr1, arr2):
    return [bin(i|j)[2:].rjust(n).replace('1','#').replace('0',' ') for i,j in zip(arr1, arr2)]


















# def solution(n, arr1, arr2):
#     return [str(bin(i | j))[2:].rjust(n,' ').replace('1','#').replace('0',' ') for i,j in zip(arr1,arr2)]