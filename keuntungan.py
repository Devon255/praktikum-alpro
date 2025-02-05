emas1 = 25
emas2 = 15
harga = 650000
harga_naik1 = 685000
harga_naik2 = 715000

total_harga = harga * emas1 
harga_sekarang = harga_naik1 * emas1 

keuntungan = harga_sekarang - total_harga 
persentase = keuntungan/total_harga * 100


harga_emas2 = emas2 * harga_naik1 
total_harga_emas = total_harga + harga_emas2
total_emas = emas1 + emas2
harga_emas3 = total_emas * harga_naik2

keuntungan2 = harga_emas3 - total_harga_emas 
persentase2 = keuntungan2/total_harga_emas * 100




print("Keuntungan pertama yang diperoleh Gerard adalah : Rp ", keuntungan)
print(f"Persentase Keuntungan pertama yang diperoleh Gerard adalah : {persentase:.2f}%")

print("Keuntungan kedua yang diperoleh Gerard adalah : Rp ", keuntungan2)
print(f"Persentase Keuntungan kedua yang diperoleh Gerard adalah : {persentase2:.2f}%")
