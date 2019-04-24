from tkinter import *
import statistics
import matplotlib.pyplot as plot

font = ('tahoma',15)
window = Tk()

window.title("statistics")

window.geometry('1000x500')

lbl = Label(window, text="Draw Histogram" , font = font)
lbl.grid(column=0, row=0)
txt = Entry(window, width=60 , font = font)
txt.grid(column=1, row=0)

def histo():

    res = list(str(txt.get()).split(','))
    sample = []

    for a in res:
        sample.append(int(a))

    print(statistics.mean(sample))
    print(statistics.median(sample))

    # plot.boxplot(sample)
    plot.hist(sample)

    plot.show()

btn = Button(window, text="Show Histogram", command=histo, font = font)
btn.grid(column=2, row=0)
window.mainloop()