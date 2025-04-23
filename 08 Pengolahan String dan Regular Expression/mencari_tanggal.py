import re

def mencari_tanggal(kalimat):
    tanggal = re.findall(r"\d{4}-\d{2}-\d{2}", kalimat)
    tahun_sekarang = 2025
    bulan_sekarang = 4
    tanggal_sekarang = 22

    def kabisat(tahun):
        return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)

    def jumlah_hari(bulan, tahun):
        if bulan == 2:
            return 29 if kabisat(tahun) else 28
        elif bulan in [4, 6, 9, 11]:
            return 30
        else:
            return 31

    def selisih_hari(thn1, bln1, tgl1, thn2, bln2, tgl2):
        selisih = 0
        if (thn1, bln1, tgl1) > (thn2, bln2, tgl2):
            thn1, bln1, tgl1, thn2, bln2, tgl2 = thn2, bln2, tgl2, thn1, bln1, tgl1
        while (thn1, bln1, tgl1) < (thn2, bln2, tgl2):
            selisih += 1
            tgl1 += 1
            hari_bulan = jumlah_hari(bln1, thn1)
            if tgl1 > hari_bulan:
                tgl1 = 1
                bln1 += 1
                if bln1 > 12:
                    bln1 = 1
                    thn1 += 1
        return selisih

    for i in tanggal:
        angka = i.split("-")
        tahun = int(angka[0])  
        bulan = int(angka[1])  
        hari = int(angka[2])    
        selisih = selisih_hari(tahun, bulan, hari, tahun_sekarang, bulan_sekarang, tanggal_sekarang)
        print(f"{hari}-{bulan}-{tahun} 00:00:00 selisih {selisih} hari")

mencari_tanggal("Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02).")