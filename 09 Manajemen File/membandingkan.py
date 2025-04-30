state = False
pembanding1 = "" 
pembanding2 = "" 
with open("09 Manajemen File\\teks1.txt") as file1,open("09 Manajemen File\\teks2.txt") as file2:
    kata1 = []
    kata2 = []
    for line1 in file1:
        kata1 += line1.strip().lower().split()
    for line2 in file2:
        kata2 += line2.strip().lower().split()

    for kata in kata1:
        if kata not in kata2:
            pembanding1 += kata + " "
            state = True
    for kata in kata2:
        if kata not in kata1:
            pembanding2 += kata + " "
            state = True
    if state == True:
        print(f"""
File1 = {line1}
File2 = {line2}
File1 ada kata "{pembanding1}" sedangkan di File2 ada kata "{pembanding2}"
""")
    else:
        print("Keduanya sama")