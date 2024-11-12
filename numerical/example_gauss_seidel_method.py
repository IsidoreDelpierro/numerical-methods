#Gauss-Seidal Method
import numpy as np
#Input
A = np.array([[1,1,1],[1,2,3],[1,4,9]])
B = np.array([3,4,6])

#Guess value of X as (1,1,1)
X = np.array([1.0, 1.0, 1.0])
print(A, "\n")
print("B = ", B, "\n")
print("X = ", np.linalg.solve(A, B))

#Lower and upper triangular matrices
L = np.tril(A)
U = A - L

#Error calculation
err = 100
while err > 0.001:
	Xn = np.dot(np.linalg.inv(L), B - np.dot(U, X))
	err = sum(abs(X - Xn))
	X = Xn

#Output
print(X)
