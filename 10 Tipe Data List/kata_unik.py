def kata_unik(folder):
    data = []
    hasil = []
    with open(folder) as file:
        for line in file:
            kata = line.lower().strip().split()
            for k in kata:
                data.append(k)
                
    for i in range (len(data)):
        k = data[i]
        jumlah = 0
        for j in range(len(data)):
            if k == data[j]:
                jumlah += 1
        if jumlah == 1:
            hasil.append(k)
    return hasil
   
print(kata_unik("10 Tipe Data List/unik.txt"))