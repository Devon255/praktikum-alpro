def palindrom(n):
    return "palindrom" if len(n) <= 1 else "bukan palindrom" if n[0] != n[-1] else palindrom(n[1:-1])

print(palindrom("katak"))
print(palindrom("ata"))
print(palindrom("pe"))
print(palindrom("kasur rusak"))
print(palindrom("komik"))