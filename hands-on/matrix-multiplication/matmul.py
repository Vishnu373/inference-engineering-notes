import numpy as np

mat1 = np.array([[0.5, 1.2, 0.3, 0.8],
                  [1.1, 0.4, 0.9, 0.2],
                  [0.7, 0.6, 1.0, 0.5]])

mat2 = np.array([[0.2, 0.8, 0.1],
                 [0.5, 0.3, 0.7],
                 [0.9, 0.4, 0.6],
                 [0.3, 0.7, 0.5]])

result = np.matmul(mat1, mat2)

print("mat1 dimension: ", mat1.shape)
print("mat2 dimension: ", mat2.shape)
print("resultant matrix dimension: ", result.shape)
