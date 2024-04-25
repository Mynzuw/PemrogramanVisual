from tkinter import *

def tidakLakukanApaApa():
    filewin = Toplevel(root)
    tombol = Button(filewin, text="Tombol tidak melakukan apa-apa")
    tombol.pack()

#Menu
root = Tk()
menubar = Menu(root)
menufile = Menu(menubar, tearoff=0)
menufile.add_command(label="Baru", command=tidakLakukanApaApa)
menufile.add_command(label="Buka", command=tidakLakukanApaApa)
menufile.add_command(label="Simpan", command=tidakLakukanApaApa)
menufile.add_command(label="Simpan sebagai...", command=tidakLakukanApaApa)
menufile.add_command(label="Tutup", command=tidakLakukanApaApa)

menufile.add_separator()
menufile.add_command(label="Keluar", command=root.quit)
menubar.add_cascade(label="Berkas", menu=menufile)
menuedit = Menu(menubar, tearoff=0)
menuedit.add_command(label="Undo", command=tidakLakukanApaApa)
menuedit.add_separator()
menuedit.add_command(label="Potong", command=tidakLakukanApaApa)
menuedit.add_command(label="Salin", command=tidakLakukanApaApa)
menuedit.add_command(label="Tempel", command=tidakLakukanApaApa)
menuedit.add_command(label="Hapus", command=tidakLakukanApaApa)
menuedit.add_command(label="Pilih Semua", command=tidakLakukanApaApa)

menubar.add_cascade(label="Sunting", menu=menuedit)
menuhelp = Menu(menubar, tearoff=0)
menuhelp.add_command(label="Indeks Bantuan", command=tidakLakukanApaApa)
menuhelp.add_command(label="Tentang...", command=tidakLakukanApaApa)
menubar.add_cascade(label="Bantuan", menu=menuhelp)

root.config(menu=menubar)

#Message
var = StringVar()
label = Message(root, textvariable=var, relief=RAISED)
var.set("Hei!? Bagaimana kabarmu?")
label.pack()

#Radio Button
def sel():
   selection = "Kamu memilihi opsi " + str(var.get())
   label.config(text = selection)
var = IntVar()
R1 = Radiobutton(root, text="Opsi 1", variable=var, value=1, command=sel)
R1.pack( anchor = W )
R2 = Radiobutton(root, text="Opsi 2", variable=var, value=2, command=sel)
R2.pack( anchor = W )
R3 = Radiobutton(root, text="Opsi 3", variable=var, value=3, command=sel)
R3.pack( anchor = W)
label = Label(root)
label.pack()

root.mainloop()