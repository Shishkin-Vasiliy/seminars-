import matplotlib.pyplot as plt
import numpy as np

k = 0,27 # коэффициент наклона
x_line = np.linspace(0,0.45,24)
y_line = k*x_line 

points = [
(0.099,0.013), (0.149,0.034), (0.199,0.049), (0.249,0.065), (0.349,0.097), (0.449,0.129), (0.099,0.015),  (0.149,0.033), (0.249,0.064), (0.349,0.098), (0.449,0.129), (0.099,0.016), (0.149,0.03), (0.199,0.048), (0.249,0.063), (0.349,0.097), (0.449,0.128), (0.099,0.015), (0.149,0.033), (0.249,0.047), (0.349,0.099), (0.449,0.128)
]

x_points = [point[0] for point in points]
y_points = [point[1] for point in points]

plt.figure(figsize=(10, 6))
plt.plot(x_line, y_line, 'b-', linewidth=2, label=f'y = {k}x')
plt.scatter(x_points, y_points, color='purple', s=50, label='Точки данных', zorder=5)

plt.xlabel('M', fontsize=12)
plt.ylabel('\u03A6', fontsize=12)
plt.title('Прямая y = 0.27x с точками данных', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)

plt.axis('equal')

plt.tight_layout()
plt.show()






