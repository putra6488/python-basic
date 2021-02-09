# merubah ke uppercase
salam = "bro"
print("normal : " + salam)
salam = salam.upper()
print("Upper : " + salam)

# merubah ke lowercase
lower = "AKSDSAJDAIsidjasodj"
print("normal : " + lower)
lower = lower.lower()
print("Lower : " + lower)

# pengecekan isX method
# pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasil akan boolean
print(salam + " is lower : " + str(apakah_lower))

# pengecekan uppercase
apakah_upper = salam.isupper()
print(salam + " is upper : " + str(apakah_upper))

# isAlpha() untuk cek semua huruf

# isalnum() untuk cek huruf dan angka

# isdecimal() untuk cek angka

# istitle() semua kata dimulai dengan huruf besar
judul = "Kaya Ilmu buat dibagi bukan kaya harta buat disombongin"
cek_judul = judul.istitle()
print(judul + " is title : " + str(cek_judul))

# cek komponen startswith() endswith()
cek_start = "KororoOtongo".startswith("KororoOtongo")
print("start : " + str(cek_start))

cek_end = "Kelapa Muda".endswith("Muda")
print("end : " + str(cek_end))

# penggabungan komponen join() split()
pisah = ['aku', 'saya', 'kamu']
gabung = ','.join(pisah)
print(gabung)