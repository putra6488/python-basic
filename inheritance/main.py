class Ojek():
    def __init__(self, nama, motor, daerah):
        self.nama = nama
        self.motor = motor
        self.daerah = daerah

    def cek_id_abang(self):
        print('nama : ', self.nama, '\nmotor : ', self.motor, '\ndaerah : ', self.daerah)

class Gojek(Ojek):
    
    def cek_id_abang(self):
        print('cek aplikasi')


ojek1 = Ojek('mario', 'honda', 'balikpapan')
ojek2 = Gojek('lili', 'yamaha', 'samarinda')

ojek1.cek_id_abang()
print(20*'=')
ojek2.cek_id_abang()