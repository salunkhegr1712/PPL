# comment 
import turtle 
t = turtle.Turtle()

class shape:
    def __init__(x, sides = 0, length = 0) :
        x.sides = sides
        x.length = length

class polygon(shape):
    
    def info(x):
        print("A polygon can be defined as a flat or plane, two-dimensional vwith straight sides.")


class square(polygon):
    def show(x):
        t.fd(x.length)
        t.rt(90)
        t.fd(x.length)
        t.rt(90)
        t.fd(x.length)
        t.rt(90)
        t.fd(x.length)
        t.rt(90)

class pentagon(polygon):
    
    def show(x):
        for i in range(5):
           t.forward(x.length) 
           t.right(72) 

class hexagon(polygon):
    
    def show(x):
        for i in range(6):
           t.forward(x.length) 
           t.right(60)
           
class octagon(polygon):
    def show(x):
        for i in range(6):
           t.forward(x.length) 
           t.right(45)

class triangle(polygon):
    def show(x):
        t.forward(x.length) 
        t.left(120)
        t.forward(x.length)
        t.left(120)
        t.forward(x.length)

figure= pentagon(3, 100)
figure.info()
figure.show()
