import matplotlib.pyplot as plt
import numpy as np

ya = 200
xa = 100
yb = 600
xb = 800


pd = int(8); pr = 255; pg = 25; pb = 255

lw = int(8); lr = 255; lg = 0; lb = 255

col = int(1000)
row = int(800)
print("col, row =", col, ", ", row)

def buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb):
    Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)
    hd = int(pd / 4)
    hw = int(lw / 4)
    dy = y2 - y1
    dx = x2 - x1

    for i in range(x1 - hd, x1 + hd):
        for j in range(y1 - hd, y1 + hd):
            if (i - x1) ** 2 + (j - y1) ** 2 < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pr
                Gambar[j, i, 2] = pr

    for i in range(x2 - hd, x2 + hd):
        for j in range(y2 - hd, y2 + hd):
            if (i - x2) ** 2 + (j - y2) ** 2 < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pr
                Gambar[j, i, 2] = pr

    if dx == 0:  # cek apakah garis vertikal
        for yi in range(min(y1, y2), max(y1, y2)):
            x = x1
            y = yi
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if (i - x) ** 2 + (j - y) ** 2 < hw ** 2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb
    else:
        my = dy / dx
        for xi in range(min(x1, x2), max(x1, x2)):
            y = int(my * (xi - x1) + y1)
            x = xi
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if (i - x) ** 2 + (j - y) ** 2 < hw ** 2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb

    return Gambar

hasil = buat_garis(ya, xa, yb, xb, pd, lw, pr, pg, pb, lr, lg, lb)


plt.figure()
plt.imshow(hasil)
plt.show()
