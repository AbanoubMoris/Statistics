from os import truncate
from tkinter import *
import statistics
import InitializeComponent as ic
from collections import Counter
import matplotlib.mlab as mlab
import matplotlib.pyplot as plot
from prettytable import PrettyTable
from tabulate import tabulate

font = ('tahoma',15)
window = Tk()
window.title("statistics")
window.geometry('1000x500')
ic.form(window)

Label(window, text="Variables  " , font = font).grid(column=0, row=0)
vartxt = Entry(window, width=60 , font = font)
vartxt.grid(column=1, row=0)

Label(window, text="Frequency  " , font = font).grid(column=0, row=1)
freqTxt = Entry(window, width=60 , font = font)
freqTxt.grid(column=1, row=1)

Label(window, text="Sample     " , font = font).grid(column=0, row=2)
sampleTxt = Entry(window, width=60 , font = font)
sampleTxt.grid(column=1, row=2)



def Sample():
    res = list(str(sampleTxt.get()).split(','))
    sample = []
    for a in res:
        sample.append(int(a))
    return sample
def frequency():
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
    plot.pie(frequency(), autopct='%1.1f%%', shadow=True, startangle=140, labels=Labels())
    plot.show()


def barChart():
    plot.bar(Labels(),frequency())
    plot.show()


def histo():

    res = list(str(sampleTxt.get()).split(','))
    sample = []

    for a in res:
        sample.append(int(a))

    plot.hist(sample)

    plot.show()



def scatterPlot():

    plot.scatter(Labels(),frequency())
    plot.show()


def boxPlot():


    res = list(str(sampleTxt.get()).split(','))
    sample = []

    for a in res:
        sample.append(int(a))
    plot.boxplot(sample)
    plot.show()

def showTable():
    t = PrettyTable()
    Class = []
    Freq = []
    sum = 0
    percent = []
    for a in Labels():
        Class.append(a)
    for a in frequency():
        Freq.append(a)
        sum+=a
    for a in frequency():
        percent.append(round(a/sum,2))
    t.add_column('Class',Class)
    t.add_column('Freq',Freq)
    t.add_column('Percent',percent)
    Label(window, text=t, font=font).grid(column=1, row=5)


#note: Historgram , Boxplot uses Sample only

Button(window, text="Show PieChart   ", command=pieChart, font = font).grid(column=2, row=0)

Button(window, text="Show BarChart   ", command=barChart, font = font).grid(column=2, row=1)

Button(window, text="Show Histogram  ", command=histo, font = font).grid(column=2, row=2)

Button(window, text="Show ScatterPlot", command=scatterPlot, font = font).grid(column=2, row=3)

Button(window, text="Show BoxPlot    ", command=boxPlot, font = font).grid(column=2, row=4)

Button(window, text="Show Table      ", command=showTable, font = font).grid(column=1, row=4)

window.mainloop()