def cek_kelas(umur):
    if umur < 4:
        return "belum cukup umur"
    elif umur < 12:
        return "SD"
    elif umur < 15:
        return "SMP"
    elif umur < 18: 
        return "SMA"
    else:
        return "Kuliah/kerja"
    
print(cek_kelas(20))
print(cek_kelas(17))
print(cek_kelas(13))
print(cek_kelas(10))
print(cek_kelas(1))




# def cek_point(point):
#     if point >= 6000:
#         return "anak sultan"
#     elif point >= 1500:
#         return "juragan"
#     elif point >= 200:
#         return "bos"
#     else:
#         return "warga"
    
# print(cek_point(5))
# print(cek_point(500))
# print(cek_point(5000))
# print(cek_point(50000))

# cek_bilangan = lambda a : "Positif" if a > 0 else "Negatif" if a < 0 else "Nol"

# print(cek_bilangan(1))
# print(cek_bilangan(-5))
# print(cek_bilangan(0))





# angka1 = int(input("Masukkan angka pertama : "))
# angka2 = int(input("Masukkan angka kedua : "))

# def penjumlahan(angka1,angka2):
#     hasil = angka1 + angka2
#     print(hasil)
#     # return hasil
    
# print(penjumlahan(angka1,angka2))