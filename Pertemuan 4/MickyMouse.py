#import library
import matplotlib.pyplot as plt
import numpy as np

#Tentukan wilayah (domain)
x = np.linspace(-12,12,10000)
plt.figure(figsize=(8,6.5))

#Tentukan persamaan matematika
y = x -x -0

#Titik pusat kepala (5,5)
y1 = 5 + (25-(x-5)**2)**0.5
y2 = 5 - (25-(x-5)**2)**0.5

#Titik pusat telinga
y3 = 9 + (4-(x-9)**2)**0.5
y4 = 9 - (4-(x-9)**2)**0.5

y5 = 9 + (4-(x-1)**2)**0.5
y6 = 9 - (4-(x-1)**2)**0.5

#kepala
plt.plot(x,y1, '-k', label='Kepala')
plt.plot(x,y2, '-k')

plt.plot(x,y3, '-k', label='Telinga Kanan')
plt.plot(x,y4, '-k')

plt.plot(x,y5, '-k', label='Telinga Kiri')
plt.plot(x,y6, '-k')

plt.fill_between(x, y1, y2, color='black', alpha=1)
plt.fill_between(x, y3, y4, color='black', alpha=1)
plt.fill_between(x, y5, y6, color='black', alpha=1)


plt.legend(loc='upper center')
plt.grid()
plt.show()


