from turtle import*
shape('triangle')

array=['red','blue','brown','yellow','grey']
for j in range(5):
    color(array[j])
    fillcolor(array[j])
    begin_fill()
    for i in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    end_fill()

    forward(50)
mainloop()
