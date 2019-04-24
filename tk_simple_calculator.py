#codeaddis.github.io/gemechis-elias/simple-python-calculator

from tkinter import * #import all from tkinter module
from math import *
def evaluate(event):
    res.configure(text = "መልስ = " + str(eval(entry.get())))
w = Tk()

#Display የምሆኑ ፁሁፎች ናቸው
Label(w, text="    Python tkinter Calculator").pack()
Label(w, text="").pack()
Label(w, text="      ቀላል የሒሳብ Calculator       ").pack()
Label(w, text=" ").pack()
Label(w, text="     ጥያቄውን ያስገቡ:       ").pack()
#-----------------------------------
entry = Entry(w) #take inpute from user

entry.bind("<Return>", evaluate)
entry.pack()
res = Label(w)
res.pack()
w.mainloop()   #end