# while : jika true terus berjalan

angka = 0

while angka < 5:
    print("nilai angka : ", angka)
    angka = angka + 1

print("di luar while")

start = True
angka = 0

while start:
    print("didalam while")
    if angka == 100:
        start = False
        print("angka 100 ketemu")
    angka += 1