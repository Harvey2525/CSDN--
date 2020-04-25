#1 For in

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
i=1
while i<=9:
    a=1
    while a<=1:
        print('{}*{}={:<4}'.format(a,i,a*i),end=' ')
        a=a+1
    i=i+1
    print('')