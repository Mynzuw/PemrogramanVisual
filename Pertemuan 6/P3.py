import numpy as np
import matplotlib.pyplot as plt

# Ukuran gambar 3x3
rowmax = 3
colmax = 3

# Membuat gambar kosong
gambar = np.zeros(shape=(rowmax, colmax, 3), dtype=np.uint8)

# Loop untuk mengisi warna berdasarkan pola tertentu
for i in range(rowmax):
    for j in range(colmax):
        if (i == 0) and (j == 0):
            gambar[i, j] = [255, 0, 0]  # Merah
        elif (i == 0) and (j == 1):
            gambar[i, j] = [0, 255, 0]  # Hijau
        elif (i == 0) and (j == 2):
            gambar[i, j] = [0, 0, 255]  # Biru
        elif (i == 1) and (j == 0):
            gambar[i, j] = [255, 255, 0]  # Kuning
        elif (i == 1) and (j == 1):
            gambar[i, j] = [255, 0, 255]  # Magenta
        elif (i == 1) and (j == 2):
            gambar[i, j] = [0, 255, 255]  # Cyan
        elif (i == 2) and (j == 0):
            gambar[i, j] = [128, 0, 0]  # Maroon
        elif (i == 2) and (j == 1):
            gambar[i, j] = [0, 128, 0]  # Hijau tua
        elif (i == 2) and (j == 2):
            gambar[i, j] = [0, 0, 128]  # Biru tua

# Menampilkan gambar
plt.imshow(gambar)
plt.axis('off')  # Menghilangkan sumbu
plt.show()
