tinggi = int(input("Masukkan tinggi: "))
lebar = int(input("Masukkan lebar: "))

def angka(tinggi, lebar):
    for i in range(1, tinggi * lebar + 1, lebar):
        print(*range(i, i + lebar))

angka(tinggi, lebar)
