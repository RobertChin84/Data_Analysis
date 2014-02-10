from numpy import *
from collections import OrderedDict
def get_data():
    #example imports =Y
    #Yt = a + b0*xt+b1*y[t-1]
    data = []#OrderedDict()
    years   = arange(1980,2000,1)
    imports = [585.6,584.2,537.4,547.8,663.3,656.4,703.8,766.1,827.3,866.2,877.3,819.2,829.6,873.8,988.4,1102.9,1159.0,1269.2,1321.9,1446.5]
    GDP     = [19603.6,20083.7,19677.5,20529.4,22020.5,22868.1,23649.6,24453.0,25473.2,26367.3,26831.6,26705.7,27520.4,28250.6,29390.9,30175.3,31252.5,32638.0,34062.6,35503.1]
    for i,year in enumerate(years):
        if i>=1:
            data.append([1.0,GDP[i],imports[i-1]])
    
    return array(data),array(imports[1:len(imports)])
    
def test_data():
    X = [[1.,6.,4.],
         [1.,10.,4.],
         [1.,12.,5.],
         [1.,14.,7.],
         [1.,16.,9.],
         [1.,18.,12.],
         [1.,22.,14.],
         [1.,24.,20.],
         [1.,26.,21.],
         [1.,32.,24.]]
    Y = [40.,44.,46.,48.,52.,58.,60.,68.,74.,80.]
    return array(X),array(Y)
def compute_coeffs(X,Y):
    n,k = X.shape
    X = mat(X)
    e = zeros(n)
    XX =  (X.T).dot(X)
    b = (XX.I).dot(X.T).dot(Y.T)
    for i,var in enumerate(Y):
        e[i] = var - X[i].dot(b.T) 
    sum_e = sum_y = 0.0
    for i,var in enumerate(e):
        sum_e+=var**2
        sum_y+=Y[i]**2
    R2 = 1.0 - sum_e/sum_y
    sb2 = ((e.T).dot(e))*(XX.I)/float(n-k)
    sbs = []
    for i in range(k-1):
        sbs.append(sb2[i][i])
    print sbs
    return array(b),R2
X,Y = test_data()#get_data()
b,R2=compute_coeffs(X,Y)
print b[0],R2
print round(b[0][0],4),round(b[0][1],4),round(b[0][2],4)

