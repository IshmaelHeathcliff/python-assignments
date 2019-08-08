import numpy as np
import scipy.signal as signal

from scipy import fftpack
from matplotlib.pyplot import plot,show

t = np.arange(-20, 20, 1/20000.0)
x = np.sin(t)
y = np.cos(t)
hx = fftpack.hilbert(x)
plot(hx)
plot(x)
plot(y)
show()