# NOT
print('=========NOT=======')
a = True
c = not a
print('data a : ' , a)
print('------NOT-------')
print('data NOT a : ' , c)

# OR (salah satu true, maka hasilnya true)
print('=========OR=======')
a = False
b = False
c = a or b
print(a, 'OR', b, '=' , c)

a = False
b = True
c = a or b
print(a, 'OR', b, '=' , c)

a = True
b = False
c = a or b
print(a, 'OR', b, '=' , c)

a = True
b = True
c = a or b
print(a, 'OR', b, '=' , c)

# AND (keduanya true, maka hasilnya true)
print('=========AND=======')
a = False
b = False
c = a and b
print(a, 'AND', b, '=' , c)

a = False
b = True
c = a and b
print(a, 'AND', b, '=' , c)

a = True
b = False
c = a and b
print(a, 'AND', b, '=' , c)

a = True
b = True
c = a and b
print(a, 'AND', b, '=' , c)

# XOR "^" (keduanya sama, maka hasilnya false)
print('=========XOR=======')
a = False
b = False
c = a xor b
print(a, 'XOR', b, '=' , c)

a = False
b = True
c = a ^ b
print(a, 'XOR', b, '=' , c)

a = True
b = False
c = a ^ b
print(a, 'XOR', b, '=' , c)

a = True
b = True
c = a ^ b
print(a, 'XOR', b, '=' , c)