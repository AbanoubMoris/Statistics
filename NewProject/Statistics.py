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

Label(window, text="Variables" , font = font).grid(column=0, row=0)
vartxt = Entry(window, width=60 , font = font)
vartxt.grid(column=1, row=0)

Label(window, text="frequancy  " , font = font).grid(column=0, row=1)
freqTxt = Entry(window, width=60 , font = font)
freqTxt.grid(column=1, row=1)

Label(window, text="sample" , font = font).grid(column=0, row=2)
sampleTxt = Entry(window, width=60 , font = font)
sampleTxt.grid(column=1, row=2)



def Sample():
    res = list(str(sampleTxt.get()).split(','))
    sample = []
    for a in res:
        sample.append(int(a))
    return sample
def frequancy():
    freq = []
    if str(freqTxt.get()) == '':
        map = dict(Counter(Sample()))
        for val in map.values():
            freq.append(int(val))
    else:
        res = list(str(freqTxt.get()).split(','))
        for a in res:
            freq.append(int(a))
    return freq

def Labels():
    labels = []
    if str(vartxt.get())=='':
        for i in Sample():
            if str(i) in labels:
                continue
            else:
                labels.append(str(i))
    else:
        labels = list(str(vartxt.get()).split(','))
    return  labels

def pieChart():
    plot.pie(frequancy(), autopct='%1.1f%%', shadow=True, startangle=140, labels=Labels())
    plot.show()


def rsma():
    plot.bar(frequancy())
    plot.show()

Button(window, text="Show PieChart ", command=pieChart, font = font).grid(column=2, row=0)

Button(window, text="Show rsma     ", command=rsma, font = font).grid(column=2, row=1)

Button(window, text="Show Histogram", command=pieChart, font = font).grid(column=2, row=2)


window.mainloop()