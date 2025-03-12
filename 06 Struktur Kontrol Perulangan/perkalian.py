angka1 = int(input("Masukkan angka yang kali: "))
angka2 = int(input("Masukkan angka pengali : "))

def perkalian(angka1,angka2):
    hasil = 0
    cara = ""
    for i in range(angka2):
        hasil = hasil + angka1
        if i == angka2 - 1:
            cara = cara + f"{angka1}"
        else: 
            cara = cara + f"{angka1} + "
    return f"Hasil dari {angka1} x {angka2} = {cara} = {hasil}"


hasil = perkalian(angka1,angka2)
print(hasil)



# angka1 = int(input("Masukkan angka : "))
# angka2 = int(input("Masukkan angka pengali : "))

# def perkalian(angka1,angka2):
#     hasil = 0
#     cara = ""
#     i = 0
#     while i < angka2:
#         hasil = hasil + angka1
#         if i == angka2 - 1:
#             cara = cara + f"{angka1}"
#         else: 
#             cara = cara + f"{angka1} + "
#         i = i + 1
#     return f"Hasil dari {angka1} x {angka2} = {cara} = {hasil}"


# hasil = perkalian(angka1,angka2)
# print(hasil)