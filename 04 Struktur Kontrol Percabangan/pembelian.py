pembelian = input("Pembelian = ")
print("Pembelian >= 100000")
try:
    pembelian = int(pembelian)
    if pembelian >= 100000:
        print(True)
    else:
        print(False)
except:
    print("Bilangan yang kamu input salah, silahkan coba lagi")