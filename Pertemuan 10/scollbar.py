from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack (side=RIGHT, fill=Y)

myList = Listbox(root, yscrollcommand= scrollbar.set)
for line in range(100):
    myList.insert(END, "This is line number " + str(line))
    
myList.pack( side = LEFT, fill = BOTH)
scrollbar.config( command=myList.yview)

mainloop()