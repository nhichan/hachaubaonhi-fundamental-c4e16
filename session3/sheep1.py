sheeps=[6,7,350,62,56,98,47]
print('hello, my name is Nhi and here are my sheep sizes: ',sheeps)
maxsize=max(sheeps)
print('now, my biggest sheep has the size of',maxsize,"lest's shear it")
sheeps.remove(maxsize)
print('after shearing, here is my flock:',sheeps)

for i in range(len(sheeps)):
    sheeps[i]+=50
print('one month has passed, here is my flock: ',sheeps)
