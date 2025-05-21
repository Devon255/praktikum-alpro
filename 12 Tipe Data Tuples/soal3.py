import re

def main(files):
    data = {}
    with open(files) as file:
        for line in file:
            jam = re.findall(r"\d{2}:\d{2}:\d{2}", line)
            if len(jam) > 0:
                jam = jam[0].split(":")[0]
                if jam in data:
                    data[jam] += 1
                else:
                    data[jam] = 1

    for key,value in sorted(data.items()):
        print(key, value)


main("12 Tipe Data Tuples\mbox-short.txt")