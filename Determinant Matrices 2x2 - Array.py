'Author: hernanda472@gmail.com'

#Matriks ukuran 2*2 dengan NumPy
import numpy as np
print("Matriks P ukuran 2*2")
P = np.array([(1,2),(3,4)])

print(P)

# Determinan Matriks
print("Determinan Matriks P ukuran 2*2")
det_P = np.linalg.det(P)

print(det_P)
