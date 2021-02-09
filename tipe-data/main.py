# Tipe Data
print('=================================')

# integer = angka yg gaada , nya
data_integer = 1

print("data : " , data_integer)
print("tipe : " , type(data_integer))

print('=================================')

# float
data_float = 1.5

print("data : " , data_float)
print("tipe : " , type(data_float))

print('=================================')

# float
data_string = "Putra Prasetyo"

print("data : " , data_string)
print("tipe : " , type(data_string))

print('=================================')

# boolean
data_bool = True

print("data : " , data_bool)
print("tipe : " , type(data_bool))

print('=================================')

# data_khusus
# bilangan kompleks
data_complex = complex(5,6)

print("data : " , data_complex)
print("tipe : " , type(data_complex))

print('=================================')

# tipe data dari bahasa C
# import dulu package nya
from ctypes import c_double, c_char, c_long 

data_c_double = c_double(10.5)
print("data : " , data_c_double)
print("tipe : " , type(data_c_double))