import turtle

def drawCurve(turtle, l,order):
    if order==0:
        turtle.forward(5)
        return
    else:
        l/=3
        drawCurve(turtle,l,order-1)
        turtle.left(60)
        drawCurve(turtle,l,order-1)
        turtle.right(120)
        drawCurve(turtle,l,order-1)
        turtle.left(60)
        drawCurve(turtle,l,order-1)





if __name__=='__main__':
    turtle.setup(800, 400)
    turtle.up()
    turtle.goto(-400,-250)
    turtle.down()
    drawCurve(turtle, 300, 4)
    turtle.exitonclick()
