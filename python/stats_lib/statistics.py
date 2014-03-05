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

def correlation(x,y,type_of_corr):
    mux   = np.mean(x)
    muy   = np.mean(y)
    N     = len(x)
    denum = N
    if type_of_corr == "sample":
        sigmax = (sample_variance(x))**0.5
        sigmay = (sample_variance(y))**0.5
        denum  = N - 1
    else:
        sigmax = np.std(x)
        sigmay = np.std(y)
        
    cov = 0.0
    for i in range(N):
        cov += (x[i] - mux)*(y[i] - muy)
    cov = cov/float(denum)
    return cov/(sigmax*sigmay)
    
def gaussian(x,mean,sigma2):
    var1 = (2.0*pi*sigma2)**0.5
    var2 = ((x-mean)**2)/2.0/sigma2
    return np.exp(-var2)/var1
    
 
def SimpleLinearReg(x,y):
    mu_x = np.mean(x)
    mu_y = np.mean(y)
    print x,y
    sum1 = 0.0
    sum2 = 0.0
    for i,x_i in enumerate(x):
        sum1+=(x_i-mu_x)*(y[i]-mu_y)
        sum2+=(x_i-mu_x)**2
    print sum1,sum2
    b = sum1/sum2
    a = mu_y - b*mu_x
    return a,b
       
    