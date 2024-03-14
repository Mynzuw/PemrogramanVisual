a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))

# Cek apakah a lebih besar dari b
print("a lebih besar dari b:", a > b)

# Cek apakah b lebih besar dari a
print("b lebih besar dari a:", b > a)

# Cek apakah a sama dengan b
print("a sama dengan b:", a == b)

# Hitung PPN a jika lebih dari 10000
ppn_a = 0.12 * a if a > 10000 else 0
print("PPN a:", ppn_a)

# Hitung PPN b jika lebih dari 50000
ppn_b = 0.12 * b if b > 50000 else 0
print("PPN b:", ppn_b)

# Tambahkan kedua PPN
total_ppn = ppn_a + ppn_b
print("Total PPN:", total_ppn)

# Hapus a dan b
del a, b

# Cek apakah a dan b sudah dihapus
print("a sudah dihapus:", 'a' not in globals())
print("b sudah dihapus:", 'b' not in globals())
