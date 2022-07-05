'Author: hernanda472@gmail.com'

# Matriks ukuran 2*2 dengan list

print('Silahkan Masukkan Matriks P 2*2: ')
print('[a0,a1]')
print('[b0,b1]')
a0 = int(input('Masukkan a0: '))
a1 = int(input('Masukkan a1: '))
b0 = int(input('Masukkan b0: '))
b1 = int(input('Masukkan b1: '))

# Matriks ukuran 2*2
a = [a0,a1]
b = [b0,b1]

#M atriks P
# x1 = [1,2]
# x2 = [3,4]

# Rumus Determinan
Det = ((a[0]*b[1] - a[1]*b[0]))
print("Determinan Matriks yang dihasilkan ialah:") 
print(Det)
