
from gturtle import *

def hoelzchen():
    setPenWidth(4)
    setPenColor("yellow")
    forward(100)
    setPenColor("red")
    dot(12)
    penUp()
    backward(100)
    penDown()

def reihe(n):
    setX(-600)
    setY(200)
    clear("black")
    repeat n:
        hoelzchen()
        penUp()
        right(90)
        forward(40)
        left(90)
        penDown()

        
def zug(spieler,n):
    while True:
        x=input(spieler+": Wie viele Hölzchen möchten Sie entfernen? (1,2 oder 3)")
        if x<=n and (x==1 or x==2 or x==3):
            break
        else:
            msgDlg("Ungültige Eingabe! Bitte wiederholen!")
    reihe(n-x)
    return n-x

def gewonnen(spieler,n):
        if n==0:
            msgDlg(spieler + " hat gewonnen.")
            return True
        return False
    
def spiel():
    n=input("Mit wie vielen Hölzchen soll gespielt werden?")
    name1=str(input("Wie heisst Spieler:in 1?"))
    name2=str(input("Wie heisst Spieler:in 2?"))
    while n>0:
        reihe(n)
        n = zug(name1,n)
        if gewonnen(name1,n):
            return name1
        n = zug(name2,n)
        if gewonnen(name2,n):
            return name2

makeTurtle()
hideTurtle()


spiel()