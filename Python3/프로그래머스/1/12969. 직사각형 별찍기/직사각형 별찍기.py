a, b = map(int, input().strip().split(' '))

# for i in range(b):
#     print('*'*a)

answer = ('*'*a+'\n')*b
print(answer)
