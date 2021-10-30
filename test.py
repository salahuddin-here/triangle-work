i = 0
sides = 8
while(i < sides):
    j = 0
    while(j < sides):      
        j = j + 1
        print('*', end = '  ')
    i = i + 1
    print('')




i = 0
sides = 8
while(i < sides):
    j = 0
    while(j < i):      
        j = j + 1
        print('*', end = '  ')
    i = i + 1
    print('')
    


rows =8

for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if(j <= rows - i):
            print(' ', end = '  ')
        else:
            print('*', end = '  ')
    print()
