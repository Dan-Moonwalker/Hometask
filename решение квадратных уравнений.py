from tkinter import *
from math import *

def click():
    a=float(textentry_a.get())
    b=float(textentry_b.get())
    c=float(textentry_c.get())
    output.delete(0.0,END)
    
    if (b**2-4*a*c)>=0:
        output.insert(END,'x1=')
        output.insert(END,(-b+sqrt(b**2-4*a*c))/(2*a))
        output.insert(END,'\nx2=')
        output.insert(END,(-b-sqrt(b**2-4*a*c))/(2*a))
    else:
        output.insert(END,'No solutions')

root = Tk()
root.title("solving quadratic equations")

Label (root, text="a", bg="black", fg="white", font="none 12 bold") .grid (row=0, column=0)
Label (root, text="b", bg="black", fg="white", font="none 12 bold") .grid (row=0, column=1)
Label (root, text="c", bg="black", fg="white", font="none 12 bold") .grid (row=0, column=2)
#create a text box
textentry_a = Entry (root, width=10, bg="white")
textentry_a.grid(row=1, column=0)
textentry_b = Entry (root, width=10, bg="white")
textentry_b.grid(row=1, column=1)
textentry_c = Entry (root, width=10, bg="white")
textentry_c.grid(row=1, column=2)

Button(root, text="SUMBIT",width=6,command=click).grid(row=2,column=0, columnspan=3)

output = Text(root, width=70, height=6, wrap=WORD, background="white")
output.grid(row=3, column=0, columnspan=3)

root.mainloop()
