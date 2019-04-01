from turtle import *

colors = ['blue', 'yellow', 'red', 'brown', 'grey']
item = -1
loop = True
while loop:
    for i in range(5):
        item +=1
        color(colors[item], colors[item])
        begin_fill()
        for i in range(2):
            forward(50)
            left(90)
            forward(100)
            left(90)
        forward(50)
        end_fill()
    if item == 4:
        loop = False
    
mainloop()