def menghitung_frekuensi(kalimat,kata):
    kalimat = kalimat.lower()
    kalimat = kalimat.split(" ")
    hasil = 0

    for i in kalimat:
        if kata in i:
            hasil += 1
    return f"{kata} ada {hasil} buah"
    

print(menghitung_frekuensi("Saya mau makan. Makan itu wajib. Mau siang atau malam saya wajib makan", "makan"))
print(menghitung_frekuensi("Saya mau makan. Makan itu wajib. Mau siang atau malam saya wajib makan", "saya"))
