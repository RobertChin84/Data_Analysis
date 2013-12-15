import numpy as np
import scipy.constants as const
pi = const.pi
def sample_variance(x):
    var = 0.0
    n    = float(len(x))
    mean = sum(x)/n
    for i in x:
        var+=(i-mean)**2
    return var/(n-1.0)
    
def gaussian(x,mean,sigma2):
    var1 = (2.0*pi*sigma2)**0.5
    var2 = ((x-mean)**2)/2.0/sigma2
    return np.exp(-var2)/var1
    
    
    