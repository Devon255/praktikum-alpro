import re

def main(file1):
    with open(file1) as file:
        email1 = []
        for line in file:
            line = line.strip()
            cari = re.findall(r"@\S+",line)
            for email in cari:
                email = email.strip(",")
                email1.append(email)
 
        kosong = {}
        for email in email1:
            if email in kosong:
                kosong[email] += 1
            else:
                kosong[email] = 1
        print(kosong)


main("11 Tipe Data Dictionary\email.txt")
