# concate
nama_pertama = "Putra "
nama_terakhir = "Prasetyo"

nama_lengkap = nama_pertama + nama_terakhir
print(nama_lengkap)

# panjang string
panjang = len(nama_lengkap)
print(panjang)

# operator keadaan untuk string
d = "a"
status = d in nama_lengkap
print(status)

# cek kebalikan in string
d = "a"
status = d not in nama_lengkap
print(status)

# mengulang string
print("wk"*10)

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-0 : " + nama_lengkap[1])
print("index ke-0 : " + nama_lengkap[2])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-1) : " + nama_lengkap[-2])
print("index ke-(-1) : " + nama_lengkap[-3])
print("index ke [0-3] : " + nama_lengkap[0:3])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))
# item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("asci code spasi : " + str(ascii_code))
data = 117
print("char untuk ascii 177 : " + chr(data))

# operator bentuk method
data = "otongo pororo"
jumlah = data.count("o")
print("Jumlah O : " + str(jumlah))