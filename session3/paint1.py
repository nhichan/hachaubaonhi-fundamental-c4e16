from turtle import*
shape('triangle')
array=['red','blue','brown','yellow','grey']
for i in range(3,7):
    color(array[i-3])
    for j in range(i):

        forward(80)
        left(360/(i))

mainloop()
print(range(3,5,1))
