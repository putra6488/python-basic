# Casting Adalah merubah tipe data dari satu tipe data ke tipe data yang lain

# INTEGER ke all

print("=============INTEGER===========")

data_int = 9
print("data = ", data_int, "type : ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)

print("data : ", data_float, "type : ", type(data_float))
print("data : ", data_str, "type : ", type(data_str))
print("data : ", data_bool, "type : ", type(data_bool))


# FLOAT ke all
# Casting akan dibulatkan ke bawah
print("=============FLOAT============")

data_float = 9.5
print("data = ", data_float, "type : ", type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)

print("data : ", data_int, "type : ", type(data_int))
print("data : ", data_str, "type : ", type(data_str))
print("data : ", data_bool, "type : ", type(data_bool))


# BOOLEAN ke all
print("=============BOOLEAN===========")

data_boolean = True
print("data = ", data_boolean, "type : ", type(data_boolean))

data_float = float(data_boolean)
data_str = str(data_boolean)
data_int = int(data_boolean)

print("data : ", data_float, "type : ", type(data_float))
print("data : ", data_str, "type : ", type(data_str))
print("data : ", data_int, "type : ", type(data_int))

# STRING ke all
print("=============STRING===========")

data_str = "0"
print("data = ", data_str, "type : ", type(data_str))

data_float = float(data_str)
data_boolean = bool(data_str)
data_int = int(data_str)

print("data : ", data_float, "type : ", type(data_float))
print("data : ", data_boolean, "type : ", type(data_boolean))
print("data : ", data_int, "type : ", type(data_int))