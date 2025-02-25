uang = 200000000
bunga = 0.1
target = 400000000


for tahun in range(1,20):
    uang += uang * bunga
    if uang >= target:
        break

print("Yang diperlukan Erika untuk cuan 400 jt adalah",tahun,"tahun")