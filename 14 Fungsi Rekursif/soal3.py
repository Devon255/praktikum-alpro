def penjumlahanGanjil(n):
    if n == 0:
        return 0
    
    if n == 1:
        print("1 = ",end='')
        return 1
    
    if n % 2 != 0:
        print(f"{n} + ",end='')
        return n + penjumlahanGanjil(n - 1)
    
    return penjumlahanGanjil(n - 1)

print(penjumlahanGanjil(7))
print(penjumlahanGanjil(10))