from numpy import *

def garch(p,q,y):
    mu = mean(y)
    et = y - mu