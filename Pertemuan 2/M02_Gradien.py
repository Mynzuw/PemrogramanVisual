import numpy as np
import matplotlib.pyplot as plt

def calculate_gradient(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def calculate_intercept(x, y, gradient):
    return y - gradient * x

def line_equation(x1, y1, x2, y2):
    gradient = calculate_gradient(x1, y1, x2, y2)
    intercept = calculate_intercept(x1, y1, gradient)
    return gradient, intercept

# Garis 1: Titik A(2, 3) dan Titik B(5, 7)
x1, y1 = 2, 3
x2, y2 = 5, 7
m1, c1 = line_equation(x1, y1, x2, y2)
print("Persamaan garis 1: y =", m1, "x +", c1)

# Garis 2: Titik C(1, 4) dan Titik D(4, 9)
x3, y3 = 1, 4
x4, y4 = 4, 9
m2, c2 = line_equation(x3, y3, x4, y4)
print("Persamaan garis 2: y =", m2, "x +", c2)

# Persiapan titik untuk plotting garis
x_values = np.linspace(-1, 6, 100)
y_values1 = m1 * x_values + c1
y_values2 = m2 * x_values + c2

# Plotting garis
plt.plot(x_values, y_values1, label='Garis 1')
plt.plot(x_values, y_values2, label='Garis 2')

# Plot titik A, B, C, dan D
plt.scatter([x1, x2, x3, x4], [y1, y2, y3, y4], color='red', label='Titik')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Visualisasi Dua Garis')
plt.legend()
plt.grid(True)
plt.show()
