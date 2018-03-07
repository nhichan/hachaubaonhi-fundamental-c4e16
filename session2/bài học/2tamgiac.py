#for i in range(6):
#    for j in range(i+1): #hoac la range bat dau t 7 va dung bien la i, twc la for i in range(7): for j in range(i+1)
#        print('*',end='')
#    print()

for i in range(6):
    for j in range(6):
        if j >=5-i:
            print('*',end='')
        else:
            print(' ', end='')
    print()
