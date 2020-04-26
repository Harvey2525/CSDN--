# 0 all multiples
print('=' * 60)
for row in range(1, 10, 1):
    for col in range(1, 10, 1):
        print("{}*{}={:<4}".format(row, col, row * col), end='')
    print('')

#0 all multiples - reversed
print('='*60)
for col in range(9, 0, -1):
    for row in range(9,0,-1):
        print("{}*{}={:<4}".format(row,col,row*col),end='')
    print('')

#1
print('='*60)
for row in range(1,10):
    for col in range(1,row+1):
        print('{}*{}={:<4}'.format(row,col,row*col),end=' ')
    print('')

#2
print('='*60)
for row in range(9,0,-1):
    for col in range(1,row+1):
        print('{}*{}={:<4}'.format(row,col,row*col),end='')
    print('')

#3
print('='*60)
for col in range(9, 0, -1):
    for row in range(1,col):
        print('{:<8}'.format(''),end='') #生成空格
    for row in range(10-col,0,-1):
        print("{}*{}={:<4}".format(row,col,row*col),end='')
    print('')

#4
print('='*60)
for col in range(9, 0, -1):
    for row in range(9-col,0,-1):
        print('{:<8}'.format(''),end='') #生成空格
    for row in range(col,0,-1):
        print("{}*{}={:<4}".format(row,col,row*col),end='')
    print('')

'''
print('='*60)
i=1
while i<=9:
    a=1
    while a<=1:
        print('{}*{}={:<4}'.format(a,i,a*i),end=' ')
        a=a+1
    i=i+1
    print('')
'''