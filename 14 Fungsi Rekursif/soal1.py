def prima(n,p = 2):
    return "prima" if p * p > n else "bukan prima" if n % p == 0 else prima(n,p+1)

print(prima(2))
print(prima(8))
print(prima(13))
print(prima(20))
print(prima(15))