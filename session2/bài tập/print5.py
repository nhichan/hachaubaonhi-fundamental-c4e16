for j in range(1,10):
    for i in range(1,10):
        result = str(i * j)
        result = result.ljust(2)
        print(result,end=' ')
    print()
