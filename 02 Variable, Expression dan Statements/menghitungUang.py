gaji_perjam = int (input("Masukkan gaji perjam yang diinginkan : "))
jam_kerja = int (input("Masukkan jumlah jam kerja yang akan dilakukan dalam 1 minggu : "))
#1
total_jam_kerja = jam_kerja * 5
pendapatan_tanpa_pajak = total_jam_kerja * gaji_perjam 
#2
pajak = pendapatan_tanpa_pajak * 0.14 
pendapatan_kena_pajak  = pendapatan_tanpa_pajak - pajak 
#3
beli_baju_aksesories = pendapatan_kena_pajak * 0.1
#4
beli_alat_tulis = pendapatan_kena_pajak * 0.01
sisa_uang = pendapatan_kena_pajak - (beli_baju_aksesories + beli_alat_tulis)
#5
sedekah = sisa_uang * 0.25 
#6
sedekah_anak_yatim = sedekah * 0.3 
#7
sedekah_kaum_dhuafa = sedekah * 0.7

print("hasil tanpa pajak : Rp %d" % (pendapatan_tanpa_pajak))
print("hasil kena pajak : Rp %d" % (pendapatan_kena_pajak))
print("uang yang akan habis untuk beli baju dan aksesories : Rp %d" % (beli_baju_aksesories))
print("uang yang akan habis untuk beli alat tulis : Rp %d" % (beli_alat_tulis))
print("uang sedekah : Rp %d" % (sedekah))
print("uang sedekah ke anak yatim : Rp %d" % (sedekah_anak_yatim))
print("uang sedekah ke kaum dhuafa : Rp %d" % (sedekah_kaum_dhuafa))