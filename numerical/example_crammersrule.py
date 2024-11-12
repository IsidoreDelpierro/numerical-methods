import numpy as np
from scipy import linalg

A = np.array([[1, 3, -2], [3, 5, 6], [2, 4, 3] ])
B = np.array([5, 7, 8])
#B = B.T
print(A, "\n")
#print(A.T, "\n\n")
print(B, "\n")
#print(B.T, "\n\n")
X = linalg.solve(A, B)
print(X, "\n===============================")

C = np.array([[2,1,-1],[1,1,2],[-1,-1,3]])
D = np.array([0,1,2]).T
Y = linalg.solve(C, D)
print(C, "\n")
print(D, "\n")
print(Y, "\n===============================")

A = np.array([[2.0,1.0,-1.0],[3.0,2.0,2.0],[4.0,-2.0,3.0]])
B = np.array([1.0,13.0,9.0])
Det  = np.linalg.det([[2.0,3.0,4.0],[1.0,2.0,-2.0],[-1.0,2.0,3.0]])
DetX = np.linalg.det([[1.0,13.0,9.0],[1.0,2.0,-2.0],[-1.0,2.0,3.0]])
DetY = np.linalg.det([[2.0,3.0,4.0],[1.0,13.0,9.0],[-1.0,2.0,3.0]])
DetZ = np.linalg.det([[2.0,3.0,4.0],[1.0,2.0,-2.0],[1.0,13.0,9.0]])

X = DetX/Det
Y = DetY/Det
Z = DetZ/Det
print("Det   = ", Det)
print("DetX  = ", DetX)
print("DetY  = ", DetY)
print("DetZ  = ", DetZ)
print("X = ", X)
print("Y = ", Y)
print("Z = ", Z, "\n")
X = linalg.solve(A, B)

print(A, "\n")
print(B, "\n")
print(X, "\n===============================")

A = np.array([[2,5],[5,-4]])
B = np.array([26,-1])
X = linalg.solve(A, B)
print(A, "\n")
print(B, "\n")
print(X, "\n===============================")

A = np.array([[3,-2],[4,-1]])
B = np.array([-4,3])
X = linalg.solve(A, B)
print(A, "\n")
print(B, "\n")
print(X, "\n===============================")
print()
