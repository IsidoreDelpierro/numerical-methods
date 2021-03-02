#Interpolation Method (Class Tutorial)
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.0, 0.4, 0.8, 1.2, 1.5, 1.8, 2.0, 2.3, 2.5, 2.7, 3.0, 3.1, 3.5, 3.7, 4.0, 4.5, 5.0])
y = np.array([0, 0.39, 0.72, 0.93, 1.00, 0.97, 0.91, 0.75, 0.60, 0.43, 0.14, 0.04, -0.35, -0.53, -0.53, -0.76, -0.98])

plt.plot(x,y)
plt.title('Graph y_values against x_values')
plt.xlabel('x_values')
plt.ylabel('y_values')
plt.show()
