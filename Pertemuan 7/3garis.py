import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menggambar garis
def gambar_garis(x1, y1, x2, y2):
    # Menghasilkan kumpulan titik-titik pada garis dengan menggunakan linspace
    x = np.linspace(x1, x2, 100)
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    y = m * x + b
    return x, y

# Menggambar garis-garis dari titik-titik yang diberikan
lines = [
    (xa, ya, xb, yb),
    (xc, yc, xd, yd),
    (xe, ye, xf, yf)
]

# Plotting
for line in lines:
    x, y = gambar_garis(*line)
    plt.plot(x, y)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Plot Garis dari Titik-titik yang Diberikan')
plt.grid(True)
plt.axis('equal')
plt.show()
