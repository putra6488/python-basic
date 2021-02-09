gorengan =["oteote", "lumpia", "pisang goreng"]

for g in gorengan:
    print(g)
    print(len(g))

# for didalam for
buah = ["jeruk", "apel", "melon", "semangka"]
sayur =["kentang", "lombok", "timun"]

daftar_belanja = [gorengan, buah, sayur]
for subdaftarbelanja in daftar_belanja:
    print(subdaftarbelanja)
    for komponen in subdaftarbelanja:
        print(komponen)