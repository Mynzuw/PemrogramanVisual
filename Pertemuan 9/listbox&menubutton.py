from tkinter import *

top = Tk()
mb= Menubutton ( top, text="condiments", relief=RAISED )
mb.grid()
mb.menu = Menu ( mb, tearoff = 0 )
mb["menu"] = mb.menu

mayoVar = IntVar()
ketchVar = IntVar()
mb.menu.add_checkbutton (label="mayo", variable=mayoVar)
mb.menu.add_checkbutton (label="ketchup", variable=ketchVar)
mb.pack()


Lb1 = Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")

Lb1.pack()
top.mainloop()