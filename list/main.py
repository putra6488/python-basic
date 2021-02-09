data = [1,2,3,4,5,6,7,8]

# akses list
Subdata = data[0]
Subdata1 = data[-1]

# memotong list
Subdata2 = data[2:4]
Subdata3 = data[-4:]

data2 = [100,200,300,400,500,600]

# menambah data list
data3 = data + data2

# merubah content dari list
data[4] = 87

# mengcopy list ke variable baru
a = data[:]
a[4] = 87

# merubah content list dengan menggunakan slicing
data[3:5] = [11,12]

# list dalam list
x = [data, data2]

# mengakses list dalam multi dimension
y = x[0][3]

# method untuk list
data.append(30)

# function untuk kepada list
panjang_list = len(data)

print(panjang_list)