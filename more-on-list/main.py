barang = ["inggris", "perancis", "indonesia", "amerika"]

print(barang)

# beberapa method untuk memanipulasi list

# menambah ke dalam list
barang.append("thailand")
print(barang)

# menambah ke list per char
barang.extend("filipina")
print(barang)

# menambahkan ke list index tertentu
barang.insert(3, "malaysia")
print(barang)

# menghitung jumlah anggota
jumlahNegara = barang.count("perancis")
print("jumlah negara : ", jumlahNegara)

# remove data
barang.remove("perancis")
print(barang)

# kebalikan urutan list
barang.reverse()
print(barang)

stuff = barang.copy()
stuff.append("gelas")
print(stuff)
print(barang)