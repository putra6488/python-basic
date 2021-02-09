def kuadrat(argumen):
    total = argumen**2
    print("nilai kuadrat argumen : ", total)
    return total

a = kuadrat(3)
print(a)

print("+"*30)

# fungsi dengan multiple argumen
def tambah(argumen1, argumen2):
    total = argumen1 + argumen2
    print(argumen1, "+", argumen2, "=", total)
    return [total]

def kali(argumen1, argumen2):
    total = argumen1 * argumen2
    print(argumen1, "X", argumen2, "=", total)
    return [total]

a = tambah(3,4)
b = kali(3,4)