def bilangan(angka):
    angka.sort(reverse=True)
    return f"tiga bilangan terbaik : {angka[0]} {angka[1]} {angka[2]}"
   
print(bilangan([5,6,3,4]))
print(bilangan([10,2,3,5,7,19,33]))





 # kosong = []
    # besar = max(angka)
    # kosong.append(besar)
    # for i in angka:
    #     if i < besar:
    #         kosong.append(i)
    # kosong.sort(reverse=True)
    
    # return f"tiga bilangan terbaik : {kosong[0]} {kosong[1]} {kosong[2]}"



    # terbesar = sorted(kosong,reverse=True)

    # return f"{terbesar[0]} {terbesar[1]} {terbesar[2]}"