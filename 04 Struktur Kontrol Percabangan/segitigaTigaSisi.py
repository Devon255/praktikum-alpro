sisi1 = input("Masukkan sisi 1 : ")
sisi2 = input("Masukkan sisi 2 : ")
sisi3 = input("Masukkan sisi 3 : ")
try: 
    sisi1 = int(sisi1)
    sisi2 = int(sisi2)
    sisi3 = int(sisi3)
    if sisi1 == sisi2 and sisi2 == sisi3:
        print("3 sisi sama")
    elif sisi1 == sisi2 or sisi2 == sisi3 or sisi1 == sisi3:
        print("2 sisi sama")
    else:
        print("Tidak ada yang sama")
except:
    print("Inputan harus berupa angka")