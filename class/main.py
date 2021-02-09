class mahasiswa():

    # public variable
    jurusan = "kecantikan"
    jumlah_mahasiswa = 0

    # private variable
    __nilai = 0

    # init = akan dijalankan saat inisialisasi objek
    def __init__(self, input_nama, input_nim):
        self.nama = input_nama #public
        self.nim = input_nim #public variable

        mahasiswa.jumlah_mahasiswa += 1

    # method
    def belajar(self, kondisi):
        print(self.nama, 'belajar', kondisi)
    
    def makan(self):
        print(self.nama, 'di kantin')

    def ujian(self, input_nilai):
        self.__nilai += input_nilai

    def uas(self, input_nilai):
        self.__nilai += input_nilai

    def cek_status(self):
        if self.__nilai <= 50:
            print(self.nama, "tidak lulus")
        else:
            print(self.nama, "anda lulus")


otong = mahasiswa("otong gatot", 12323)
ucup = mahasiswa("ucup surucup", 42423)
ale = mahasiswa("ale con", 34543)

mahasiswa.jurusan = "ekonomi"
otong.hobi ="menyanyi"

otong.ujian(10)
otong.uas(50)

otong.cek_status()

print(otong.jurusan)
print(otong.nama)
print(otong.nim)
print(otong.hobi)
print(mahasiswa.jumlah_mahasiswa)

otong.belajar("sangat rajin")

ucup.ujian(50)
ucup.uas(0)
ucup.cek_status()