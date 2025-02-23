import numpy as np

matriks = np.array([[1, 2, 3],
                    [0, 1, 4],
                    [5, 6, 0]])

invers = np.linalg.inv(matriks)

print("Matriks:")
print(matriks)
print("Invers Matriks:")
print(invers)