#  operasi biner

a = 9
b = 5

# OR (|)
c = a | b
print("==========OR=========")
print("nilai A : ", a, "binary : ", format(a, "08b"))
print("nilai B : ", b, "binary : ", format(b, "08b"))
print("Hasil A or B : ", c, "binary : ", format(c, "08b"))

# AND (&)
c = a & b
print("==========AND=========")
print("nilai A : ", a, "binary : ", format(a, "08b"))
print("nilai B : ", b, "binary : ", format(b, "08b"))
print("Hasil A and B : ", c, "binary : ", format(c, "08b"))

# XOR (^)
c = a ^ b
print("==========AND=========")
print("nilai A : ", a, "binary : ", format(a, "08b"))
print("nilai B : ", b, "binary : ", format(b, "08b"))
print("Hasil A xor B : ", c, "binary : ", format(c, "08b"))

# NOT (~)
c = ~a
print("==========NOT=========")
print("nilai A : ", a, "binary : ", format(a, "08b"))
print("Hasil not A : ", c, "binary : ", format(c, "08b"))
d = 0b0000001001
e = 0b1111111111
print("nilai : ", e^d, "binary : ", format(e^d, '08b'))

# shifting
# shift right
c = a >> 1
print("==========>>=========")
print("nilai A : ", a, "binary : ", format(a, "08b"))
print("Hasil Shift Right A : ", c, "binary : ", format(c, "08b"))

# shift left
c = a << 1
print("==========>>=========")
print("nilai A : ", a, "binary : ", format(a, "08b"))
print("Hasil Shift Left A : ", c, "binary : ", format(c, "08b"))