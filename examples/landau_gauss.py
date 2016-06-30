# Plot the Landau Gauss convolution (Langau) and cross check with convolution with scipy

import numpy as np
import pylandau
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter1d

mpv, eta, sigma, A = 10, 1, 3, 1
x = np.arange(0, 50, 0.01)
y = pylandau.landau(x, mpv=mpv, eta=eta, A=A)
y_gconv = gaussian_filter1d(y, sigma=sigma / 0.01)
y_gconv_2 = pylandau.langau(x, mpv, eta, sigma, A)
plt.plot(x, y, label='Landau')
plt.plot(x, y_gconv_2, label='Langau')
plt.plot(x, y_gconv, '--', label='Langau Scipy')
plt.legend(loc=0)
plt.show()
