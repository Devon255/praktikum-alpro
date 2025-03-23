n = int(input("Masukkan n : "))


def primaTerdekat(n):
    if n <= 2:
        print("Tidak ada bilangan prima terdekat")
    else:
        for i in range(n-1,1,-1):
            for j in range(2,i):
                if i % j == 0:
                    break
            else:
                print(i,end=" ")
                break


primaTerdekat(n)