def rata2():
    kosong = []

    while True:
        data = input("Masukkan angka : ")
        if data.lower() == "done":
            rata = sum(kosong)/len(kosong)
            break
        try:
            angka = int(data)
            kosong.append(angka)
        except:
            return "input tidak valid"
    return rata

hasil = rata2()
print(hasil)