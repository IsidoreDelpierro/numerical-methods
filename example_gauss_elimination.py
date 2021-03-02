#Gauss Elimination
import numpy as np
A = np.array([[1,2,-1],[2,1,4],[3,3,4]])
B = np.array([1,2,1])
print(A, "\n")
print("B = ", B, "\n")
print("X = ", np.linalg.solve(A, B))
