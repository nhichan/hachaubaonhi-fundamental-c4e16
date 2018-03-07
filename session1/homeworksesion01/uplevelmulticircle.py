from turtle import *

shape('triangle')
color('green')
speed(-3)
tron = int(input('hay nhap so hinh tron ban muon ve:'))
#nhập càng nhiều càng đẹp
for i in range (tron):
    circle(100)
    left(360/tron)

mainloop()
