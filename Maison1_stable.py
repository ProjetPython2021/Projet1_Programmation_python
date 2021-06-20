import dessinMSDA  as d
#from decorMaison import *
d.t.speed(11)
d.t.color("black")


d.t.fillcolor("grey")
d.t.begin_fill()
d.allez(0-500,-100-200)
d.rectangle(50, 10)
d.rectangle(250, 10)
d.rectangle(350, 10)
d.t.end_fill()


d.t.fillcolor("cyan")
d.t.begin_fill()
d.allez(0-500, -90-200)
d.rectangle(350, 265)
d.t.end_fill()


d.t.fillcolor("white")
d.t.begin_fill()
d.allez(120-500, -90-200)
d.rectangle(100, 150)
d.t.end_fill()

d.t.fillcolor("white")
d.t.begin_fill()
d.allez(250-500, 15-200 )
d.carre(45)
d.t.end_fill()
d.t.fillcolor("white")
d.t.begin_fill()
d.allez(250-500, -30-200 )
d.carre(45)
d.t.end_fill()
d.t.fillcolor("white")
d.t.begin_fill()
d.allez(295-500, 15-200 )
d.carre(45)
d.allez(295-500, -30-200 )
d.carre(45)
d.t.end_fill()

d.t.fillcolor("pink")
d.t.begin_fill()
d.allez(-35-500, 175-200)
d.triangle(420, 200)
d.t.end_fill()


d.t.fillcolor("grey")
d.t.begin_fill()
d.allez(0-240, 45)
d.rectangle(50, 100)
d.t.end_fill()






d.t.done()
