print("List menjadi Set")
data_list1 = ["aku","kamu","saya","semua"]
print("Sebelum : ",data_list1)
data_set1 = set(data_list1)
print("Sesudah : ",data_set1)

print()

print("Set menjadi List")
data_set2 = {"angka","huruf","simbol"}
print("Sebelum : ",data_set2)
data_list2 = list(data_set2)
print("Sesudah : ",data_list2)

print()

print("Tuple menjadi Set")
data_tuple1 = (1,2,3)
print("Sebelum : ", data_tuple1)
data_set1 = set(data_tuple1)
print("Sesudah : ",data_set1)

print()

print("Set menjadi Tuple")
data_tuple2 = {1,2,3,4}
print("Sebelum : ", data_tuple2)
data_set2 = tuple(data_tuple2)
print("Sesudah : ",data_set2)