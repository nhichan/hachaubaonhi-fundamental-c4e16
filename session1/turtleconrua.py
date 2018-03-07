from turtle import *

shape('turtle')
color('blue')
speed(-1)

fillcolor('yellow')
canh = int(input("muon nhap bao nhieu canh: "))
begin_fill()
for i in range(canh):
        forward(100)
        left(360/canh)

end_fill()
mainloop()
