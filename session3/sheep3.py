sheeps=[6,7,350,62,56,98,47]
print('hello, my name is Nhi and here are my sheep sizes: ',sheeps)

for j in range(3):
    maxsize=max(sheeps)

    print('now, my biggest sheep has the size of',maxsize,"lest's shear it")
    for index,item in enumerate(sheeps):
        if item==maxsize:
            sheeps[index]=8


    print('after shearing, here is my flock:',sheeps)

    print('MONTH',j+1)
    for i in range(len(sheeps)):
        sheeps[i]+=50
    print('one month has passed, here is my flock: ',sheeps)


tong = sum(sheeps)
print('my flock has size in total: ',tong)
price= tong*2
print('I would get',tong,'* 2$ =',str(price)+'$')
