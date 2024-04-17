import numpy as np

A = np.array([[1,1,2],[2,1,0],[4,1,2]])
B = np.array([[2,5,7],[2,8,0],[4,3,1]])
print(A)
print(B)
print(A+B)
print(np.matmul(A,B)) # A@B, A.dot(B)
print(A*B)
print(np.transpose(A))
print(np.linalg.inv(A))
print(A**5)
print(np.power(A,5))
print(np.linalg.matrix_power(A,5))
print(np.linalg.det(B))
print(np.linalg.matrix_power(B,-3))

C = np.array([[1],[2],[4]])
D = np.array([2,5,7])
# print(C@D) błąd
print(D@C)
print(C*D)
print(C+D)

E = np.array([[1,5],[2,1]])
F = np.array([[2,1],[2,8]])
print(E/F)
print(E//F)
print(E%F)