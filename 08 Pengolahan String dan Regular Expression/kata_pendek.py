def kata_pendek(kalimat):
    kata = kalimat.split()
    kata_terpendek = kata[0]  
    kata_terpanjang = kata[0]

    for kata in kata:
        if len(kata) < len(kata_terpendek):
            kata_terpendek = kata
        elif len(kata) > len(kata_terpanjang):
            kata_terpanjang = kata
        else:  
            continue

    return f"kata terpendek {kata_terpendek} dan kata terpanjang {kata_terpanjang}"



print(kata_pendek("red snakes and a black frog in the pool"))