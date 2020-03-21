import numpy as ny
x0=ny.ones((10),dtype=ny.int16)
x1=[64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03]
x2=[2,3,4,2,3,4,2,4,1,3]
y=ny.array([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])
X=ny.stack((x0,x1,x2),axis=1)
Y=y.reshape(10,1)
X=ny.mat(X)
Y=ny.mat(Y)
W=((X.T*X).I)*X.T*Y
print(X)
print(Y)
print(W)
print(W.shape)