import matplotlib.pyplot as plt
import numpy as np

x1 = 100
y1 = 100
x2 = 500
y2 = 500

lw = int(10)

hw = int(lw/2)

row = int(1000)
col = int(1000)
print('col, row =', col, ',', row)

Gambar = np.zeros(shape=(row,col,3), dtype=np.int16)
Gambar[:, :, :] = 255

Gambar[y1,x1, :] = 0
Gambar[y2,x2, :] = 0
Gambar[y1, x1, 0] = 255
Gambar[y2, x2, 0] = 255

for i in range(x1-hw,x1+hw):
    for j in range(y1-hw,y1+hw):
        if ( (i-x1)**2 + (j-y1)**2 ) < hw **2:
            Gambar[j,i,:] = 0
            Gambar[j,i,0] = 255



for i in range(x2-hw,x2+hw):
    for j in range(y2-hw,y2+hw):
        if ( (i-x2)**2 + (j-y2)**2 ) < hw **2:
            Gambar[j,i,:] = 0
            Gambar[j,i,0] = 255

plt.figure()
plt.imshow(Gambar)
plt.show()
