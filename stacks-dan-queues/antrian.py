from collections import deque

antrian = deque([1,2,3,4,5])
print("data sekarang : ", antrian)

# menambahkan data
antrian.append(6)
print("data masuk : ", 6)
print("data sekarang : ", antrian)

antrian.append(7)
print("data masuk : ", 7)
print("data sekarang : ", antrian)

# mengurangi antrian = kurangin yang depan
out = antrian.popleft()
print("data keluar : ", out)
print("data sekarang : ", antrian)
out = antrian.popleft()
print("data keluar : ", out)
print("data sekarang : ", antrian)
out = antrian.popleft()
print("data keluar : ", out)
print("data sekarang : ", antrian)

antrian.append(8)
print("data masuk : ", 7)
print("data sekarang : ", antrian)