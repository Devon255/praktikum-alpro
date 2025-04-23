import re
import random

def mencari_email(email):
    email = email.lower()
    cari = re.findall("\S+@\S+",email)


    def password(panjang = 8):
        huruf_kecil = "abcdefghijklmnopqrstufwxyz"
        huruf_kapital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        angka = "0123456789"
        gabung = huruf_kecil + huruf_kapital + angka
        pw = ""
        for j in range(panjang):
            acak = random.choice(gabung)
            pw += acak
        return pw

    for i in cari:
        usn = i.split("@")[0]
        pw = password()
        print(f"{i}, username : {usn}, password : {pw}")


        


mencari_email("Berikut adalah daftar email dan nama pengguna dari mailing list: anton@mail.com dimiliki oleh antonius budi@gmail.co.id dimiliki oleh budi anwari slamet@getnada.com dimiliki oleh slamet slumut matahari@tokopedia.com dimiliki oleh toko matahari")
