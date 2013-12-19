import numpy as np
from scipy.stats import distributions


def compute_p_value(fobs,DFG,DFE):
    f_value = distributions.f.cdf(fobs, DFG, DFE)
    p_value = 1.0 - f_value
    return p_value

def compute_f_crit(alpha,DFG,DFE):
    return distributions.f.ppf(1.0-alpha, DFG, DFE)    

def anova(data,alpha):
    n_dim         = len(data)
    SSE           = 0.0
    total_average = 0.0
    N             = 0
    n_array       = {}
    av_i          = {}
    for group in data:
        d              = data[group]
        n_array[group] = len(d)
        av_i[group]    = np.mean(d)
        total_average  += av_i[group]*n_array[group]
        N              += n_array[group] 
        for x in d: 
            SSE+=(x-av_i[group])**2
        
    total_average/=N
    SSG = 0.0
    for group in av_i:
        SSG+=n_array[group]*(av_i[group]-total_average)**2
    DFE = N - n_dim
    DFG = n_dim - 1
    MSE = SSE/float(DFE)
    MSG = SSG/float(DFG)
    F_obs  = MSG/MSE
    p_value = compute_p_value(F_obs,DFG,DFE)
    F_crit  = compute_f_crit(alpha,DFG,DFE)
    print "Null hypothesis that the averages don't show statistical differences"
    if p_value>alpha:
        print "Reject null hypothesis for a confidence level {0}".format(alpha)
    else:
        print "Accept null hypothesis for a confidence level {0}".format(alpha)
    print "p_value: {0}".format(p_value)
    print "F_obs: {0} F_crit: {1}".format(F_obs,F_crit)
    return [F_obs,F_crit,p_value] 


""""
test_case:http://math.colgate.edu/math102/dlantz/examples/ANOVA/anovanc.html
data = {}
data['Sam'] = [364,245,284,172,198,239,259,188,256,263,329,136,272,245,209,298,342,217,358,412,382,593,261]
data['Lou'] = [260,204,221,285,308,262,196,299,316,216,155,212,201,175,241,233,279,368,413,240,243,325,156,280]
data['Mac'] = [156,438,272,345,198,137,166,236,168,269,296,236,275,269,142,184,301,262,258]  

anova(data,0.05)
"""
