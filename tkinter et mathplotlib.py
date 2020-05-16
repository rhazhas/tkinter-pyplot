from tkinter import *
from matplotlib.pyplot import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from math import cos,pi


fen= Tk()
fen.size=(1200,500)
fen.title("Gestionnaire d'images")

X=[x for x in range(200)]
Y=[cos(2*pi*i/100) for i in X]
f=figure()
plot(X,Y)

figureTK = FigureCanvasTkAgg(f, fen)
figureTK.get_tk_widget().pack(side=LEFT, fill=BOTH)

fen.mainloop()