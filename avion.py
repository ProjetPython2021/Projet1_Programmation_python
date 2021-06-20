#Programme python pour dessiner un avion avec le module turtle
#import du module dessinMSDA
import dessinMSDA as d
#import du module turtle
from turtle import *
#import du module math
import math
d.t.bgcolor("skyblue")
fillcolor("blue")
begin_fill()
A=d.t.pos()
d.t.rt(-45)
d.t.fd(100)
#end_fill
#fillcolor("blue")
#begin_fill
d.demi_cercle(30)
#end_fill
#fillcolor("blue")
#begin_fill
d.t.fd(100)
d.t.rt(60)
d.t.fd(95)
d.t.rt(-65)
d.t.fd(20)
d.t.rt(-100)
d.t.fd(80)
d.t.rt(110)
d.t.fd(80)
d.t.rt(65)
d.t.fd(50)
d.t.rt(-65)
d.t.fd(35)
d.t.rt(-120)
d.t.fd(90)
d.t.rt(45)
d.t.fd(90)
d.t.rt(-120)
d.t.fd(35)
d.t.rt(-65)
d.t.fd(50)
d.t.rt(80)
d.t.fd(80)
d.t.rt(110)
d.t.fd(80)
d.t.rt(-100)
d.t.fd(20)
goto(A[0],A[1])
end_fill()


d.t.done()