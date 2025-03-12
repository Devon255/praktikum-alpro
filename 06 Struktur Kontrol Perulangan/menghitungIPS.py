jumlah = int(input("Masukkan jumlah matakuliah : "))

def menghitung_ips(jumlah):
    total_bobot = 0
    for i in range(1,jumlah + 1):
        nilai = input(f"Nilai MK {i} : ").lower()
        if nilai == "a":
            bobot = 4
        elif nilai == "b":
            bobot = 3
        elif nilai == "c":
            bobot = 2
        elif nilai == "d":
            bobot = 1
        total_bobot = total_bobot + bobot
    ips = round (total_bobot / jumlah,2)
    print(f"Nilai IPS anda semester ini {ips}")

menghitung_ips(jumlah)