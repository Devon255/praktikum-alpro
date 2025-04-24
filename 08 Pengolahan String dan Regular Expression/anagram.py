def anagram(kata, perbandingan):
    kata = kata.lower()
    perbandingan = perbandingan.lower()
    
    if len(kata) != len(perbandingan):
        return False
    else:
        for huruf in kata:
            if kata.count(huruf) != perbandingan.count(huruf):
                return False
        return True


print(anagram("mata","atma"))
print(anagram("mata","maat"))
print(anagram("mata","taam"))
print(anagram("mata","tama"))
print(anagram("mata","katma"))
