nama_band = [
    "payung teduh",
    "fourtwenty",
    "peterpan",
    "dmasiv"
    ]

lagu =[
    "akad",
    "fana merah jambu",
    "cobalah mengerti",
    "jangan menyerah"
    ]

# enumerate

print(20*"=")

for i,band in enumerate(nama_band):
    print(i,':',band)

# zip = menggabungkan 2 buah list

print(20*"=")

for band,lagu in zip(nama_band,lagu):
    print(band,'menyanyikan lagu yang berjudul : ', lagu)

print(20*"=")

playlist = {'terendap laraku', 'resah jadi luka', 'zona nyaman', 'pelangi dimatamu'}

for lagu in sorted(playlist):
    print(lagu)

# dictionary

print(20*"=")

playlist2 = {
    "payung teduh":"akad",
    "fourtwenty":"fana merah jambu",
    "peterpan":"cobalah mengerti",
    }

for i,v in playlist2.items():
    print(i,'lagunya : ', v)

for i in reversed(range(1,10,1)):
    print(i)