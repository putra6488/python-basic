# Input yang dimasukkan user pasti bernilai string

# string
data = input("Masukkan Nama : ")
print("data : " , data, "type : ", type(data))

# mengambil tipe data int / float
angka = int(input("masukkan angka : "))
angka = float(input("masukkan angka : "))
print("data : " , angka, "type : ", type(angka))

# boolean
# casting ke int lalu boolean
biner = bool(int(input("massukan nilai boolean : ")))
print("data : " , biner, "type : ", type(biner))