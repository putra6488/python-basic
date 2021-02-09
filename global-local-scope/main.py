# scope variable local

namaIkan = "ito"

def rubahNamaIkan(namaBaru):
    namaIkan = namaBaru
    print("saya ganti nama ikan jadi : ", namaIkan)

rubahNamaIkan("ani")
print("nama ikan jadi : ", namaIkan)

print(20*"=")

# global
namaKucing = "loi"
makanKucing = "whiskas"

def rubahNamaKucing(Baru):
    global namaKucing
    namaKucing = Baru
    print("saya ganti nama ikan jadi : ", namaKucing)

def kasihMakanKucing(makanan, nama):
    global namaKucing, makanKucing
    namaKucing = nama
    makanKucing = makanan


rubahNamaKucing("miss")
kasihMakanKucing("royal canin", "ale")
print("nama kucing jadi : ", namaKucing, "makanannya : ", makanKucing)