#Case 1
print("Case 1")
#Date bertipe boolean yang kita deklarasikan (Cara standar)
f = bool(True)
q = bool(False)
print(f)
print(q)
print("=================================================")

#Case 2
print("Case 2")
#Data bertipe boolean dalam berbagai konteks
#Tercatat dengan sendirinya oleh komputer tanpa deklarasi
print(3>2)
print(3+2==5)
print(3<2)
print("=================================================")

#Case 3
print("Case 3")
#Data bertipe Boolean dalam berbagai konteks
#Tercatat dengan sendirinya oleh komputer tanpa deklarasi
Penghasilan = 20000000
PenghasilanTanpaPajak = 4000000
if Penghasilan <= PenghasilanTanpaPajak:
    PajakYangHarusDibayar = 0
if Penghasilan > PenghasilanTanpaPajak:
    PajakYangHarusDibayar = 0.1 * Penghasilan
print("Pajak yang dibayar: Rp", PajakYangHarusDibayar)

#Case 4
print("Case 4")
#Semua data yang tidak nol (kosong) memiliki nilai boolean true
a = 3                                                           #integer
b = "Ini data string"                                           #string
c = ("Laptop", "Buku", "Ballpen")                               #tuple
d = ["Laptop", "Buku", "Ballpen"]                               #list
e = {"Laptop": "asus", "Buku": "buku_teks", "Ballpen": "arrow"} #dictionary
f = {1,2,3,4,5}
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))

#Case 5
print("Case 5")
#Variabel yang kosong memiliki nilai Boolean False
a = 0                                               #integer null
b = ""                                              #stribg kosong
c = ()                                              #tuple kosong
d = []                                              #list kosong
e = {}                                              #dictionary kosong
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print("============================================")

#Case 6
print("Case 6")
#Variabel yang panjangnya nol memiliki nilai Boolean False
class myclass():
    def __len__(self):
        return 0
print(bool(myclass()))
print("============================================")
