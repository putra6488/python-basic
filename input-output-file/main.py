# INPUT OUTPUT FILE

# membuat file text

# w = write
# r = read
# a = appending = menambahkan data di akhir baris
# r+ = write and read

file = open("data.txt", 'w')

# write
file.write("ini adalah data text dibuat dengan python")
file.write("\nini baris kedua")

file.close()

# reading
file2 = open("data.txt", 'r')

print(file2.read())
print(file2.readline())

file2.close()

# appending
file3 = open("data.txt", 'a')

file3.write("\nbaris ini dibuat dengan append mode")

file3.close()