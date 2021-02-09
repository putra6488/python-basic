# dictionary = 

member1 = {
    "id":101,
    "nama":"putra prasetyo",
    "pekerjaan":"mahasiswa",
    "status":"premium"
}

member2 = {
    "id":102,
    "nama":"bambang sumantri",
    "pekerjaan":"karyawan",
    "status":"biasa"
}

memberlist = {101:member1,102:member2}

print(member1.items())
print(member1["nama"])
print(member1.keys())
print(member1.values())

print(memberlist)