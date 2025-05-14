def main(list1,list2):
    data = {}
    n = 0
    for key in list1:
        for value in list2[n:n+1]:
            data[key] = value
            n += 1
    
    hehe = ["green", "blue", "red"]
    hasil = {}
    
    for j in hehe:
        hasil[j] = data[j]
    
    print(hasil)



lista = ['red','green','blue']
listb = ['#FF0000','#008000', '#0000FF']
main(lista,listb)