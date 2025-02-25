tinggi = float (input("Masukkan tinggi badan anda : "))
bmi = float (input("Masukkan BMI yang diharapkan : "))

berat_diperlukan = bmi * (tinggi ** 2)

print("Jika tinggi badan %.2f m, Maka berat yang diperlukan adalah %.2f kg" % (tinggi,berat_diperlukan))
