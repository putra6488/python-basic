print("program pembagian")

while True:
    try:
        penyebut = int(input("masukkan angka penyebut : "))
        pembilang = int(input("masukkan angka pembilang : "))
        hasil = penyebut/pembilang
        
        break

    # error apapun diambil dan dikasih tau
    except Exception as err:
        print(err)

    # ambil errornya dan dikasihtau
    except ValueError:
        print("yang anda masukkan bukan angka")
    except ZeroDivisionError:
        print("angka yang anda masukan nol")

print("berhasil", hasil)