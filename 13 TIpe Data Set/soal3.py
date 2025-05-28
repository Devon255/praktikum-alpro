def main():
    data1 = input("Masukkan judul file : ").lower()
    data2 = input("Masukkan judul file : ").lower()
    akses1 = f"13 TIpe Data Set\\{data1}"
    akses2 = f"13 TIpe Data Set\\{data2}"
    try:
        with open(akses1) as file1, open(akses2) as file2:
            for line1 in file1:
                print("File 1 = ", line1.lower())
            for line2 in file2:
                print("File 2 = ", line2.lower())
    except:
        print("Eror, File tidak ditemukan")
        
main()