from turtle import*
shape('triangle')

for i in range(3,7):
    if i%2==0:
        color('red')
    else:
        color('blue')
    for j in range(i):

        forward(80)
        left(360/(i))

mainloop()
print(range(3,5,1))
