bulan = input("Masukkan bulan (1-12) : ")
try: 
    bulan = int(bulan)
    if bulan <= 12:
        if bulan == 2:
            print("Jumlah hari : 29")
        elif bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12:
            print("Jumlah hari : 31")
        elif bulan == 3 or bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11:
            print("Jumlah hari : 30")
    else:
        print("Bulan yang anda masukkan tidak ada")
except:
    print("Inputan ini harus angka")