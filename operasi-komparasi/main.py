a = 4
b = 2

# >
print("=============Lebih Dari============")
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = b > 2
print(b, '>', 2, '=', hasil)

# <
print("=============Kurang Dari============")
hasil = a < 3
print(a, '<', 3, '=', hasil)
hasil = b < 3
print(b, '<', 3, '=', hasil)
hasil = b < 2
print(b, '<', 2, '=', hasil)

# >=
print("=============Lebih Dari, Sama Dengan============")
hasil = a >= 3
print(a, '>=', 3, '=', hasil)
hasil = b >= 3
print(b, '>=', 3, '=', hasil)
hasil = b >= 2
print(b, '>=', 2, '=', hasil)

# <=
print("=============Kurang Dari, Sama Dengan============")
hasil = a <= 3
print(a, '<=', 3, '=', hasil)
hasil = b <= 3
print(b, '<=', 3, '=', hasil)
hasil = b <= 2
print(b, '<=', 2, '=', hasil)

# =
print("=============Sama Dengan============")
hasil = a == 3
print(a, '==', 2, '=', hasil)
hasil = b == 3
print(b, '==', 3, '=', hasil)
hasil = b == 2
print(b, '==', 2, '=', hasil)

# !=
print("=============Tidak Sama Dengan============")
hasil = a != 3
print(a, '!=', 2, '=', hasil)
hasil = b != 3
print(b, '!=', 3, '=', hasil)
hasil = b != 2
print(b, '!=', 2, '=', hasil)

# is
print("=============IS Komparasi Object Identity============")
x = 5
y = 5
print("nilai x = ", x, ',id', hex(id(x)))
print("nilai y = ", y, ',id', hex(id(y)))

hasil_is = x is y
print("x is y = ", hasil_is)


x = 5
y = 6
print("nilai x = ", x, ',id', hex(id(x)))
print("nilai y = ", y, ',id', hex(id(y)))

hasil_is = x is y
print("x is y = ", hasil_is)

# is not
print("=============IS NOT Komparasi Object Identity============")
x = 5
y = 5
print("nilai x = ", x, ',id', hex(id(x)))
print("nilai y = ", y, ',id', hex(id(y)))

hasil_is = x is not y
print("x is y = ", hasil_is)


x = 5
y = 6
print("nilai x = ", x, ',id', hex(id(x)))
print("nilai y = ", y, ',id', hex(id(y)))

hasil_is = x is not y
print("x is y = ", hasil_is)