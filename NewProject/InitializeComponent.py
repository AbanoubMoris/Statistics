from tkinter import *
def form(frm):

    frm.update()
    fw = frm.winfo_width()
    fh = frm.winfo_height()
    sw = frm.winfo_screenwidth()
    sh = frm.winfo_screenheight()
    x = (sw - fw) /2
    y = (sh - fh) /2 -45

    frm.title("statistics")
    frm.geometry('%dx%d+%d+%d' % (fw,fh,x,y))