def main(angka):
    jumlah = 0
    for i in angka:
        if i == angka[0]:
            jumlah += 1
    
    if jumlah == len(angka):
        print(True)
    else:
        print(False)
        

main((90,90,90,90))
main((80,70,80,80))
main((70,70,70,10))