import inline
import matplotlib
from lib2to3.pgen2.tokenize import Double
from os import truncate
from tkinter import *
import statistics
import InitializeComponent as ic
from collections import Counter
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from tabulate import tabulate
import csv
from collections import defaultdict
import math
import numpy as np
from scipy import stats




def ReadData():
    columns = defaultdict(list)

    with open('12.csv') as f:
        reader = csv.DictReader(f) # read rows into a dictionary format
        for row in reader:
            for (k,v) in row.items():
                try:
                    columns[k].append(int(v))
                except:
                    pass
    return columns

plt.pie(ReadData()['Sample'])
plt.show()

font = ('tahoma',15)
window = Tk()
window.title("statistics")
window.geometry('1000x500')
ic.form(window)

Label(window, text="Variables  ", font=font).grid(column=0, row=0)
vartxt = Entry(window, width=60, font=font)
vartxt.grid(column=1, row=0)

Label(window, text="Frequency  ", font=font).grid(column=0, row=1)
freqTxt = Entry(window, width=60, font=font)
freqTxt.grid(column=1, row=1)

Label(window, text="Sample     ", font=font).grid(column=0, row=2)
sampleTxt = Entry(window, width=60, font=font)
sampleTxt.grid(column=1, row=2)

Label(window, text="X     ", font=font).grid(column=0, row=4)
X_Txt = Entry(window, width=60, font=font)
X_Txt.grid(column=1, row=4)

Label(window, text="Y     ", font=font).grid(column=0, row=5)
Y_Txt = Entry(window, width=60, font=font)
Y_Txt.grid(column=1, row=5)


def Sample():
    res = list(str(sampleTxt.get()).split(','))
    if res == '':
        res =ReadData()['Sample']
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
    plt.pie(frequency(), autopct='%1.1f%%', shadow=True, startangle=140, labels=Labels())
    plt.show()

def barChart():
    plt.bar(Labels(),frequency())
    plt.show()

def histo():

    res = list(str(sampleTxt.get()).split(','))
    sample = []
    for a in res:
        sample.append(int(a))
    plt.hist(sample)
    plt.show()

def scatterPlot():

    plt.scatter(Labels(),frequency())
    plt.show()


def boxPlot():
    res = list(str(sampleTxt.get()).split(','))
    sample = []
    for a in res:
        sample.append(int(a))
    plt.boxplot(sample)
    plt.show()

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
    win = Tk()
    win.title("Table")
    win.geometry('500x500')
    ic.form(win)
    Label(win, text=t, font=font).grid(column=0, row=0)


def X_Values():
 listX = []
 if str(X_Txt.get()) == '':
    map = dict(Counter(len(listX)))
    for val in map.values():
        listX.append(int(val))
 else:
  res = list(str(X_Txt.get()).split(','))
  for a in res:
    listX.append(int(a))
 return listX

def Y_Values():
 listY = []
 if str(Y_Txt.get()) == '':
    map = dict(Counter(len(listY)))
    for val in map.values():
        listY.append(int(val))
 else:
  res = list(str(Y_Txt.get()).split(','))
  for a in res:
    listY.append(int(a))
 return listY


def corr_comment(r):
    if(r >=0.9 or r < -0.9):
        comment.set("Perfrct")
    elif(r >= 0.7 and r <= 0.9):
         comment.set("Strong")
    elif (r >= 0.4 and r <= 0.6):
        comment.set("Modrate")
    else:
        comment.set("Weak")


corr = StringVar()
Corr_lbl = Label
comment = StringVar()
Com_lbl = Label

x = []
y = []

def Show_R():

    x = X_Values()
    y = Y_Values()
    N=len(x)
    sumX = 0
    sumY = 0
    sumXY = 0
    sumXsqr = 0
    sumYsqr = 0
    for i in range(0,len(x)):
        sumX += x[i]
        sumY += y[i]
        sumXY += x[i]*y[i]
        sumXsqr += x[i]*x[i]
        sumYsqr += y[i]*y[i]

    sumxALLsqr = sumX*sumX
    sumYALLsqr = sumY*sumY

    R = (N *(sumXY)-(sumX*sumY)) / math.sqrt((N*(sumXsqr-sumxALLsqr)*(N*(sumYsqr-sumYALLsqr))))
    corr.set(R)
    corr_comment(R)


#12,8,5,3,2,0
#1,7,4,6,4,2

def linear_reg():
    x = np.array(X_Values())
    y = np.array(Y_Values())
    slop, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    plt.plot(x, y, 'ro', color='red')
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.axis([0, 100, 0, 100])
    plt.plot(x, x*slop + intercept, 'b')
    plt.plot()
    plt.show()

#note: Historgram , Boxplot uses Sample only

frama = Frame(window , bg = 'gray')
b1 = Button(frama, text="Show PieChart       ", command=pieChart, font=font)
b2 = Button(frama, text="Show BarChart      ", command=barChart, font=font)
b3 = Button(frama, text="Show Histogram    ", command=histo, font=font)
b4 = Button(frama, text="Show ScatterPlot   ", command=scatterPlot, font=font)
b5 = Button(frama, text="Show BoxPlot        ", command=boxPlot, font=font)
frama.grid(row=0, column=2, rowspan=3)

b1.grid(column=0, row=0)
b2.grid(column=0, row=1)
b3.grid(column=0, row=2)
b4.grid(column=0, row=3)
b5.grid(column=0, row=4)
#b6.grid(column=0, row=5)

b6 = Button(window, text="Show Table      ", command=showTable, font=font).grid(column=1, row=3)
Corr_lbl = Label(window, textvariable=corr, font=font)
Com_lbl = Label(window, textvariable=comment, font=font)
Corr_lbl.grid(column=2, row=6)
Com_lbl.grid(column=2,row=7)

f = Frame(window, bg='gray')
b7 = Button(f, text="Correlation      ", command=Show_R, font=font)
b8 = Button(f, text="linear Regression    ", command=linear_reg, font=font)
f.grid(row=7, column=1)

b7.grid(column=0, row=0)
b8.grid(column=1, row=0)

window.mainloop()