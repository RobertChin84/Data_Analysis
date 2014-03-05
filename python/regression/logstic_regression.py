from numpy import *


"""
def loadDataSet():
    data = [];label =[];
    fr   = open('./data/logistic_test_data/ex2data1.txt')
    for line in fr.readlines():
        row = line.strip().split(',')
        data.append([1.0,float(row[0]),float(row[1])])
        label.append(int(row[-1]))
    return data,label
    
"""
def sigmoid(z):
    return 1.0/(1.0-e**(-1.0*z))

def compute_cost(theta,X,y):
    m = X.shape[0]
    theta = reshape(theta,(len(theta),1))
    var   = X.dot(theta)
    J = (1.0/m)*( (-(y.T).dot(log(sigmoid(var)))) - ((1.0-y).T).dot(log(1.0-sigmoid(var))))
    grad = ()((1.0/m)*(sigmoid(var) - y)).T).dot(X)
    return J[0][0]
    
def compute_grad(theta,dataIn,labels):
    y = labels
    X = dataIn
    m = len(X[0])
    theta.shape = (1,m)
    grad = zeros(m)
    h = sigmoid(X.dot(theta.T))
    delta  = h - y
    l = grad.size
    
    for i in range(l):
        sumdelta = (delta.T).dot(X[:,i])
        grad[i]  = (1.0/m)
        
        
        
        
def gradDescent(dataIn,classLabels,alpha):
    data   = mat(dataIn)
    labels = mat(classLabels).T
    m,n    = shape(data)
    maxCycles = 500
    weights   = ones((n,1))
    print data*weights
    for k in range(maxCycles):
        
        h       = sigmoid(data*weights)
        
        error   = (label - h)
        weights = weights + alpha*data.T*error
    return weights 
    
data,label = loadDataSet()
gradDescent(data,label,0.05)
