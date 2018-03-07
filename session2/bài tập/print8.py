num=int(input('nhap 1 so: '))
for i in range(num):
    for j in range(num):
        print(1 - ((i+j)% 2), end=' ')
    print()
