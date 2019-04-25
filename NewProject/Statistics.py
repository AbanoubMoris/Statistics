from tkinter import *
import statistics
import InitializeComponent as ic
from collections import Counter
import matplotlib.mlab as mlab
import matplotlib.pyplot as plot

font = ('tahoma',15)
window = Tk()
window.title("statistics")
window.geometry('1000x500')
ic.form(window)

lbl = Label(window, text="Draw Histogram" , font = font)
lbl.grid(column=0, row=0)
txt = Entry(window, width=60 , font = font)
txt.grid(column=1, row=0)

def Sample():
    res = list(str(txt.get()).split(','))
    sample = []
    for a in res:
        sample.append(int(a))
    return sample
def frequancy():
    map = dict(Counter(Sample()))
    x = []
    for val in map.values():
        x.append(int(val))
    return  x
def Labels():
    labels = []
    for i in Sample():
        if str(i) in labels:
            continue
        else:
            labels.append(str(i))
    return  labels
def pieChart():
    plot.pie(frequancy(), autopct='%1.1f%%', shadow=True, startangle=140, labels=Labels())
    plot.show()


Button(window, text="Show Histogram", command=pieChart, font = font).grid(column=2, row=0)

Button(window, text="Show Histogram", command=pieChart, font = font).grid(column=2, row=0)

Button(window, text="Show Histogram", command=pieChart, font = font).grid(column=2, row=0)


window.mainloop()