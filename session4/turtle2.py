from turtle import*
shape('circle')
color('blue')
speed(-1)
for j in range(50):
    for i in range(4):
        forward(3+j*2)
        left(90)
    left(10)
mainloop()
