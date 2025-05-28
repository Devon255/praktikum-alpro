def playstore():
    pilih = int(input("Masukkan Berapa Kategori : "))
    aplikasi = {
        "RPG":["Honkai Star Rail", "Wuthering Waves", "Genshin Impact"],
        "Strategi":["Valorant", "Mobile Legend", "PUBG", "Clash of Clans"],
        "Moba":["Mobile Legend", "League Of Legends", "Dota"],
        "Adventure":["Genshin Impact", "Minecraft", "Wuthering Waves", "Roblox"],
        "Kreatif":["Minecraft", "Roblox"]
    }

    kategori_terpilih = []
    for i in range(1, pilih + 1):
        kategori = input(f"Masukkan nama kategori ke {i} : ")
        kategori_terpilih.append(kategori)
    
    data = {}
    for key,value in aplikasi.items():
        for j in kategori_terpilih:
            if j.lower() == key.lower():
                data[key] = value

    hasil = []
    for k in data.values():
        hasil.extend(k)

    key = list(data.keys())
    kategori1 = set(data[key[0]])
    kategori2 = set(data[key[1]])
    
    print(f"""
Kategori 1 : {", ".join(kategori1)}
Kategori 2 : {", ".join(kategori2)}
Game yang ada di kedua kategori : {", ".join(kategori1 & kategori2)}
Game yang hanya ada di 1 kategori : {", ".join(kategori1 ^ kategori2)}
""")

playstore()