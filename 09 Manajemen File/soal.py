nama_soal = input("nama file1 : ")
jenis_soal = "soal.txt"
state = False

with open("09 Manajemen File\soal2.txt") as file:
    for line in file:
        line2 = line.strip().split("||")
        soal = line2[0].strip().lower()
        jawaban = line2[1].strip().lower()
        if nama_soal.lower() == jenis_soal.lower():
            print(f"{soal}")
            jawab = input("Jawab : ").strip()
            if jawab == jawaban:
                print("Jawaban benar!")
                state = True
            else:
                print("Jawaban salah")
                continue
if not state:
    print("Jenis soal tidak ditemukan")

