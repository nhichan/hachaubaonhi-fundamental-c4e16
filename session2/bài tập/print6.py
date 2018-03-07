num = int(input('nhap 1 so: '))
for j in range(1,(num+1)):
    for i in range(1,(num+1)):
        result = str(i * j)
        result = result.ljust(2)
        print(result,end=' ')
    print()
