import numpy as np
X=np.array([
        [1,7,680],
        [1,8,61],
        [1,9,73],
        [1,10,76],
        [1,11,61],
        [1,12,65],
        [1,13,69],
        [1,14,62],
        [1,15,81],
        [1,16,64],
        [1,17,71],
        [1,18,82]])

Y=np.array([
        13.5,
        14.3,
        14.7,
        14.8,
        14.9,
        15.2,
        15.5,
        16.8,
        17.3,
        17.7,
        18.3,
        18.6 ])

X_tr=X.T
X_tr_X=X_tr.dot(X)
X_tr_X_revers=np.linalg.inv(X_tr_X)
X_tr_Y=X_tr.dot(Y)
A=X_tr_X_revers.dot(X_tr_Y)
print("Вектор оценок А = ", A)

Y_end=X.dot(A)
print("Y = ", Y)
print("Y_end = ", Y_end)