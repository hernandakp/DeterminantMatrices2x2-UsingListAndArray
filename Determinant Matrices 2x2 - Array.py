print("Nama          : Hernanda Khoiriyah Putri")
print("NIM           : 1306620025")
print("Mata Kuliah   : Pemrograman Komputer")
print("Dosen Pengampu: Dewi Muliyati, M.Si., M.Sc.")
print("Case 1 - Determinant of 2 x 2 Matrices")
print("-------------------------------------------")

#Matriks ukuran 2*2 dengan NumPy
import numpy as np
print("Matriks P ukuran 2*2")
P = np.array([(1,2),(3,4)])

print(P)

# Determinan Matriks
print("Determinan Matriks P ukuran 2*2")
det_P = np.linalg.det(P)

print(det_P)
