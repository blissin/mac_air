import numpy as np

A=[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,0,0]]
B=[1,1,1,1,1]
A=np.array(A)
B=np.array(B)
X=np.linalg.lstsq(A, B, rcond = -1)
# print(np.linalg.inv(np.dot(A.T,A)))
# k=np.dot(np.dot(np.linalg.inv(np.dot(A.T,A)),A.T),B)
print (X)
# print(k)
y=np.array([19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24])
print(y.shape)
