# Importation du module<<TURTLE>> 
import turtle
t = turtle
t.speed(2)

def allez(x,y,angle=0):
    '''
    OBJECTIF : cette fonction permet d'aller la tortue,sans tracer, a un point de coordonnees(x et y)

    METHODE: utilisation des methodes "penup()", "goto()", " angle()", pendown()
    BESOIN:"o" comme position actuelle du curseur, "x" comme abcise du point et "y" comme ordonnee, "z" comme
    CONNUS: /
    ENTREE: o,x,y et z
    RESULTAT: /
    HYPOTHESE: o,x,y et z sont des nombres reels
    '''
    t.penup()
    t.goto(x,y)
    t.lt(angle)
    t.pendown()


def rectangle(l, h):
    '''
    OBJECTIF: tracer un rectangle dans le repere
    METHODE: utilisation de le methode de circle 
    BESOIN: "l" et "h"
    CONNUS : /
    ENTREE: l et h 
    RESULTAT: /
    HYPOTHESE: l et h sont des nombres reels
    '''
    for i in range(2):
        t.forward(l)
        t.left(90)
        t.forward(h)
        t.left(90)


def carre(c):
    '''
    OBJECTIF: tracer un carre dans le repere 
    METHODE: utilisation de la methode circle
    BESOIN: "c"
    CONNUS: /
    ENTREE: c
    RESULTAT: /
    HYPOTHESE: c est un nombre reel
    '''
    for i in range(4):
        t.forward(c)
        t.left(90)


def cercle(r):
    '''
    OBJECTIF:tracer un cercle dans un repere 
    METHODE: utilisation de la methode circle
    BESOIN: "r"
    CONNUS: /
    ENTREE: r
    RESULTAT: /
    HYPOTHESE: r est un nombre reel

    '''
    t.circle(r)

def demi_cercle(r):
    '''
    OBJECTIF: tracer un demi cercle dans un repere
    METHODE: utilisation de le methode circle
    BESOIN: "r"
    CONNUS: /
    ENTREE: r
    RESULTAT: /
    HYPOTHESE: r est un nombre reel
    '''

    t.circle(r, 180)


def triangle(c, hauteur):
    '''
    OBJECTIF: tracer un triangle dans un repere
    METHODE: utilisation de le methode "goto", "forward'"
    BESOIN : "c" et "hauteur"
    CONNUS: /
    ENTREE: c et hauteur
    RESULTAT: /
    HYPOTHESE: c et hauteur sont des nombres reels
    '''

    x = t.xcor()
    y = t.ycor()
    t.forward(c)
    t.goto(x+(c/2), y+hauteur)
    t.goto(x, y)


def polygone(c, n):
    '''
    OBJECTIF: tracer un polygone dans un repere
    METHODE: utilisation des boucles et des methode "forward"  et "left"
    BESOIN: "c" et "n"
    CONNUS: /
    ENTREE: c et n
    RESULTAT:
    HYPOTHESE: c et n sont des nombres reels
    '''
    for i in range(n):
        t.forward(c)
        t.left(360/n)


def trapeze(c1, c2, c3, ang):
    '''
    OBJECTIF: tracer un trapeze dans un repere
    METHODE: utilisation des methodes "backward","left","forward","right"
    BESOIN : "c1","c2","c3" et ang
    CONNUS: /
    ENTREE: c1 c2 c3 et ang
    RESULTAT: /
    HYPOTHESE: c1,c2,c3 et ang sont des nombres reels
    '''

    x = t.xcor()
    y = t.ycor()
    t.backward(c1)
    t.left(ang)
    t.forward(c2)
    t.right(ang)  
    t.forward(c3)
    t.goto(x, y)


    def parallelogramme(long, hauteur, angle):
        '''
        OBJECTIF : tracer un parallelogramme
        METHODE : utilisation d'affectations de boucle ainsi que les methodes "forward","left","penup"et "position"
        BESOIN : "long","hauteur", et "angle"
        CONNUS : /
        ENTREE : long hauteur et angle
        SORTIE : x
        RESULTAT : /
        HYPOTHESE : "long","hauteur", et "angle" sontdes nombres reels
        '''
        origine = turtle.pos()
        y=turtle.ycor()
        turtle.fd(long)
        turtle.lt(angle)
        turtle.penup()
        while (y < origine[1] + hauteur):
            turtle.fd(1)
            y=turtle.ycor()
            turtle.pendown()
            x=turtle.xcor()
            turtle.goto(origine[0]+long,origine[1])
            turtle.goto(+x,origine[1]+hauteur)
            turtle.lt(-angle)
            turtle.bk(long)
            turtle.goto(origine[0],origine[1])
    return x

def losange(c, ang):
    '''
    OBJECTIF: tracer un losange dans un repere
    METHODE: utilisation des boucles et des methodes "left";"forward"
    BESOIN : "c" et "ang"
    CONNUS: /
    ENTREE: c et ang
    RESULTAT: /
    HYPOTHESE: c et ang sont des nombre des reels
    '''
    x = t.xcor()
    y = t.ycor()
    for i in range(2):
        t.left(ang)
        t.forward(c)
    t.left(180-ang)
    t.forward(c)
    t.goto(x, y)


def ellipse(r):
    '''
    OBJECTIF:trcer un ellipse dans un repere
    METHODE: utilisation de la methode circle
    BESOIN: "r"
    CONNUS: /
    ENTREE: r
    RESULTAT: /
    HYPHOTHESE: r est un nombre reel
    '''
    t.right(45)
    for i in range(2):
        t.circle(r, 90)
        t.circle(r / 2, 90)


