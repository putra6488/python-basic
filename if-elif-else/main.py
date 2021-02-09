nilai = 60

if nilai == 75:
    print("nilai : ", nilai)

if nilai != 60:
    print("nilai : ", nilai)

print(20*"=")
if 80 <= nilai <= 100:
    print("nilai a : ")
elif 70 <= nilai < 80:
    print("nilai b : ")
elif 60 <= nilai < 70:
    print("nilai c : ")
elif 50 <= nilai < 60:
    print("nilai d : ")
else:
    print("gagal lulus")

print(20*"=")
print("operator logika untuk string dan list")

gorengan =["oteote", "lumpia", "pisang goreng"]
beli = "lumpia"

# cek nilai didalam list
if beli in gorengan:
    print("saya beli itu makanan")

if not beli in gorengan:
    print("aiss")

# cek char
char = 'u'
if char in beli:
    print("ada")
else:
    print("tidak ada")