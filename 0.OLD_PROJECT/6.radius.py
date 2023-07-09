from scipy.interpolate.rbf import Rbf  # radial basis functions
import matplotlib.pyplot as plt
import numpy as np

x = [1, 1, 2 ,3, 4, 4, 2, 6, 7]
y = [0, 2, 5, 6, 2, 4, 1, 5, 2]
z = [1]*len(x)

rbf_adj = Rbf(x, y, z, function='gaussian')

x_fine = np.linspace(0, 10, 10)
y_fine = np.linspace(0, 10, 10)

x_grid, y_grid = np.meshgrid(x_fine, y_fine) # mesh grid 형성 linspace로 잘게 쪼갠만큼 표현
# print(x_grid,'\n')
# print(y_grid)

# z_grid = rbf_adj(x_grid.ravel(), y_grid.ravel()).reshape(x_grid.shape)
z_grid = rbf_adj(x_grid, y_grid)

# print(z_grid)

plt.pcolor(x_fine, y_fine, z_grid);
plt.plot(x, y, 'o');
plt.xlabel('x'); plt.ylabel('y'); plt.colorbar();
plt.title('RBF Gaussian interpolation');
plt.show()