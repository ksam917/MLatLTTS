
import scipy
print('scipy: %s' % scipy.__version__)

import numpy
print('numpy: %s' % numpy.__version__)

import matplotlib
print('matplotlib: %s' % matplotlib.__version__)

import pandas
print('pandas: %s' % pandas.__version__)

import statsmodels
print('statsmodels: %s' % statsmodels.__version__)

import sklearn
print('sklearn: %s' % sklearn.__version__)



import numpy as np 
#Importing the fft and inverse fft functions from fftpackage
from scipy.fftpack import fft
from scipy.fftpack import ifft

#create an array with random n numbers
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])

#Applying the fft function
y = fft(x)
print y

yinv = ifft(y)
print yinv
