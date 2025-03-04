angka1 = int(input("Masukkan angka pertama : "))
angka2 = int(input("Masukkan angka kedua : "))
angka3 = int(input("Masukkan angka ketiga : "))

def cek_angka(angka1,angka2,angka3):
    if angka1 + angka2 == angka3:
        return True
    elif angka1 + angka3 == angka2:
        return True
    elif angka3 + angka1 == angka2:
        return True
    elif angka3 + angka2 == angka1:
        return True
    else:
        return False

print(cek_angka(angka1,angka2,angka3))
# print(cek_angka(1,2,3))
# print(cek_angka(4,5,6))
# print(cek_angka(3,2,1))
# print(cek_angka(9,7,3))
