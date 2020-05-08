#flocon de Von Koch
import turtle

def segment(l,n):
    """trace d'un segment
    input
    l:taille du segment
    n:ordre du flocon
    output
    """
    if n==0:
        turtle.forward(l)
    else:
        segment(l/3,n-1)
        turtle.left(60)
        segment(l/3,n-1)
        turtle.right(120)
        segment(l/3,n-1)
        turtle.left(60)
        segment(l/3,n-1)

def flocon(l,n):
    """
    regroupement de segment
    input
    l:taille
    n: ordre
    output
    """
    segment(l,n)
    turtle.right(120)
    segment(l,n)
    turtle.right(120)
    segment(l,n)

#initialisation de la turtle
turtle.setup(800, 400)
turtle.up()
turtle.goto(-280,80)
turtle.down()

#données:nombres d'etapes et longueur du cote initial
etape=int(input('n=')) #n=4
taille=float(input('l=')) #500
flocon(taille,etape)
turtle.up()
turtle.goto(800,400)

turtle.exitonclick()
