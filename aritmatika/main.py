a = 10
b = 3

# tambah
hasil = a + b
print(a, '+', b, '=', hasil)

# kurang
hasil = a - b
print(a, '-', b, '=', hasil)

# perkalian
hasil = a * b
print(a, 'X', b, '=', hasil)

# bagi
hasil = a / b
print(a, '/', b, '=', hasil)

# operasi eksponen (**) pangkat
hasil = a ** b
print(a, 'pangkat', b, '=', hasil)

# modulus
hasil = a % b
print(a, '%', b, '=', hasil)
 
# floor = pembagian yang dibulatkan
hasil = a // b
print(a, 'floor division', b, '=', hasil)

# prioritas operasi
# 1. ()
# 2. eksponen
# 3. perkalian
# 4. pertambahan

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // y
print(x, '**', y, '*', z, '+', x, '/', y, '-', y, '%', z, '//', y, '=', hasil )