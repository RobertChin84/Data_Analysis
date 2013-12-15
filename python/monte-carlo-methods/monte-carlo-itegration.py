from random import *
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const

##Compute the area under the curve with monte-carlo method.
pi = const.pi
def f(x):
    return (np.cos(x))**2
    
def compute_error(I_actual,I_mc):
    return 100.0*(I_actual - I_mc)/I_actual
def monte_carlo(N):
    #compute the integral with monte-carlo
    x_min,x_max = [0.0,pi]
    f_max       = 1.0
    counter     = 0
    random_pairs = [[random(),random()] for i in range(N)]
    for i,v in enumerate(random_pairs):
        x_r = v[0]*(x_max-x_min) + x_min
        f_r = v[1]*f_max
        if f_r <= f(x_r):
            counter+=1
    I_mc = float(counter)*f_max*(x_max-x_min)/float(N)
    return I_mc
    
