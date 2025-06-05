def jumlahDigit(n):
    if n == 0:
        return 0
    
    if n < 10:
        print(f"{n} = ",end='')
        return n 

    if n >= 10:
        print(f"{n % 10} + ",end='')
        
    return jumlahDigit(n // 10) + n % 10
    
print(jumlahDigit(9084))
print(jumlahDigit(234))
print(jumlahDigit(5))
print(jumlahDigit(0))