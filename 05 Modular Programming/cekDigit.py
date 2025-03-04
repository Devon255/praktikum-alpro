angka1 = int(input("Masukkan angka pertama : "))
angka2 = int(input("Masukkan angka kedua : "))
angka3 = int(input("Masukkan angka ketiga : "))

def cek_digit_belakang(angka1,angka2,angka3):
    if angka1 % 10 == angka2 % 10:
        return True
    elif angka2 % 10 == angka3 % 10:
        return True
    elif angka3 % 10 == angka1 % 10:
        return True
    else:
        return False

print(cek_digit_belakang(angka1, angka2, angka3))

# print(cek_digit_belakang(30, 20, 18))
# print(cek_digit_belakang(145, 5, 100)) 
# print(cek_digit_belakang(71, 187, 18))
# print(cek_digit_belakang(1024, 14, 94))
# print(cek_digit_belakang(53, 8900, 658))