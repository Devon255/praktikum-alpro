def main(data):
    nama = data[0]
    nim = data[1]
    alamat = data[2]

    print(f"""
NIM : {nim}
NAMA : {nama}
ALAMAT : {alamat}
""")
    
    nim = tuple(nim)
    print(f"NIM : {nim}")

    nama_depan = nama.split()[0]
    nama_depan = tuple(nama_depan)
    print(f"NAMA DEPAN : {nama_depan[1:]}")
   
    nama_terbalik = nama.split()
    nama_terbalik = tuple(nama_terbalik)
    print(f"NAMA TERBALIK : {nama_terbalik[::-1]}")


data_diri = ("Devon Novan Surya Putra", "71241115", "Wonocatur, DI Yogyakarta")
main(data_diri)