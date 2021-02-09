# ------0++++++++5--------8++++++++11----------

inputUser = float(input("masukkan angka : \n lebih dari 0 kurang dari 5 \n lebih dari 8 kurang dari 11 \n adalah : "))

isKurangDari5 = (inputUser < 5)
print(isKurangDari5)

isLebihDari0 = (inputUser > 0)
print(isLebihDari0)

isKurangDari11 = (inputUser < 11)
print(isKurangDari11)

isLebihDari8 = (inputUser > 8)
print(isLebihDari8)

# lebih dari 10 kurang dari 3 (3 - 10 = salah)
isCorrect = isKurangDari5 and isLebihDari0 and isKurangDari11 and isLebihDari8
print("angka yang anda masukkan : ", isCorrect)