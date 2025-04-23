def spasi_normal(kalimat):
    kalimat = kalimat.split(" ")
    for i in kalimat:
        if i.isalpha():
            print(i, end=" ")
    print()




spasi_normal("saya   tidak  suka      memancing             ikan")
