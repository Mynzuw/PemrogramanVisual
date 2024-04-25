from tkinter import *
from tkinter import messagebox
top = Tk()

my_var = StringVar()
L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5, textvariable=my_var)
E1.pack(side = LEFT)

CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = "Music", variable = CheckVar1, \
   onvalue = 1, offvalue = 0, height=5, \
   width = 20, )
C2 = Checkbutton(top, text = "Video", variable = CheckVar2, \
   onvalue = 1, offvalue = 0, height=5, \
   width = 20)
C1.pack()
C2.pack()

top.geometry("350x300")
def helloCallBack():
   msg=messagebox.showinfo( "Hello Python", "Hello, " + my_var.get() )
B = Button(top, text ="Hello", command = helloCallBack)
B.place(x=250,y=250)


frame = Frame(top)
frame.pack()

bottomframe = Frame(top)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)

var = StringVar()
label = Label( top, textvariable=var, relief=RAISED )
var.set("Hey!? How are you doing?")
label.pack()


top.mainloop()