from turtle import *

shape('triangle')
color('blue')
speed(-1)

fillcolor('yellow')
begin_fill()
for i in range(4):
    forward(150)
    left(90)

end_fill()
mainloop()
