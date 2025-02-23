import numpy as np

#Membuat Array/Matriks
#Membuat Matriks 3x3
matriks = np.array([[1, 2, 3],
                    [0, 1, 4],
                    [5, 6, 0]])

#Menghitung Invers
invers = np.linalg.inv(matriks)

#Cetak Hasil nya
print("Matriks:")
print(matriks)
print("Invers Matriks:")
print(invers)