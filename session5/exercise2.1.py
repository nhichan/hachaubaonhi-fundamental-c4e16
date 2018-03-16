numbers=[1,6,8,1,2,1,5,6]
print('numbers =',numbers)
find=int(input('nhap 1 so muon tim: '))

count=0
for i in range(len(numbers)):
    if numbers[i]==find:
        count+=1

print(find,'appears',count,'times in my list')
