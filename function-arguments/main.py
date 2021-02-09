def siswa(nama):
    print("nama siswa : ", nama)

siswa('putra')
print(30*"=")

# fungsi dengan keyword arguments

def guru(nama, kaprodi):
    print("nama guru : ", nama)
    print("prodi : ", kaprodi)

guru(nama='ita', kaprodi="tkj")
guru(nama='ani', kaprodi="adm")
print(30*"=")

# fungsi dengan default argumen

def wali_kelas(nama, kelas="pagi", umur=10):
    print("nama guru : ", nama)
    print("kelas : ", kelas)
    print("umur : ", umur)

wali_kelas('pino')
wali_kelas('sutoyo', kelas="malam", umur=99)