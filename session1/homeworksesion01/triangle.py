from turtle import *

shape('triangle')
color('blue')
speed(-1)

fillcolor('yellow')
begin_fill()
for i in range(3):
    forward(150)
    left(120)

end_fill()
mainloop()
