# Membuat Gabungan rentang dari sebuah angka

inputUser = float(input("Masukkan angka yang bernilai kurang dari 3 atau lebih 10 : "))

# angka kurang dari 3
isKurangDari = (inputUser < 3)
print(isKurangDari)

# angka lebih dari 10
isLebihDari = (inputUser > 10)
print(isLebihDari)

# lebih dari 10 kurang dari 3 (3 - 10 = salah)
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukkan : ", isCorrect)

# 3 - 10 true
inputUser = float(input("Masukkan angka yang bernilai kurang dari 3 dan lebih 10 : "))

# lebih dari 3
isLebihDari =  inputUser > 3
print("Lebih dari 3 : ", isLebihDari)

# kurang dari 10
isKurangDari =  inputUser < 10
print("Lebih dari 3 : ", isKurangDari)

# lebih dari 3 kurang dari 10 (1 - 3 = salah, lebih dari 10 = salah)
isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukkan : ", isCorrect)