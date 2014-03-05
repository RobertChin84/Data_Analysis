import numpy as np

def GradientDescent(X,y,theta,alpha,num_iters):
    #update theta based on:
    #X = 
    #y = training data
    #theta 
    #alpha = 
    #num_iters = max iterations to converage
    m = len(y)
    for i in range(0,num_iters):
        h1 = h(theta,x) - y
        for k,v in enumerate(theta):
            v = v - (alpha/float(m))*sum()