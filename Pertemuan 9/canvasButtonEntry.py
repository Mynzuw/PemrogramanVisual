import tkinter as tk

root = tk.Tk()

#Membuat Canvas
Frameku = tk.Frame(root, bg = 'blue')
Frameku.place(relwidth = 1, relheight = 1)


#Membuat Button
Tombolku = tk.Button(Frameku, text = "Tes Tombol", bg = 'gray', fg = 'red')
Tombolku.pack()


#Membuat Entry
Entryku = tk.Entry(Frameku, bg = 'green')
Entryku.pack()

root.mainloop()