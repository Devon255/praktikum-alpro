import math

uang = 200 
bunga = 0.1
target = 400

tahun_yang_dibutuhkan = math.log(target/uang)/math.log(1+bunga)

print(f"Yang diperlukan Erika untuk cuan 400 jt adalah {tahun_yang_dibutuhkan:.2f}tahun")

