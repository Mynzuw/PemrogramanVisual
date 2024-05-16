import tkinter as tk

root = tk.Tk()

Frameku = tk.Frame(root, bg = '#7469B6')
Frameku.place(relwidth = 0.95, relheight = 0.95)

Tombolku = tk.Button(Frameku, text = "Tes Tombol", bg = '#FFE6E6', fg = '#AD88C6')
Tombolku.pack()

Entryku = tk.Entry(Frameku, bg="#E1AFD1")
Entryku.pack()

root.mainloop()