print("Nama          : Hernanda Khoiriyah Putri")
print("NIM           : 1306620025")
print("Mata Kuliah   : Pemrograman Komputer")
print("Dosen Pengampu: Dewi Muliyati, M.Si., M.Sc.")
print("Case 1 - Determinant of 2 x 2 Matrices")
print("-------------------------------------------")

#Matriks ukuran 2*2 dengan list
print('Silahkan Masukkan Matriks P 2*2: ')
print('[a0,a1]')
print('[b0,b1]')

a0 = int(input('Masukkan a0: '))
a1 = int(input('Masukkan a1: '))
b0 = int(input('Masukkan b0: '))
b1 = int(input('Masukkan b1: '))

#Matriks ukuran 2*2
a = [a0,a1]
b = [b0,b1]

#Matriks P
#x1 = [1,2]
#x2 = [3,4]

#Rumus Determinan
Det = ((a[0]*b[1] - a[1]*b[0]))
print("Determinan Matriks yang dihasilkan ialah:") 
print(Det)
