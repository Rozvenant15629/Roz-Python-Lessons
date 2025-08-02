chuoi = input("nhap vao mot chuoi bat ki: ")
chu_hoa = 0
for a in chuoi:
    if a.isupper():
        chu_hoa = chu_hoa + 1
print("co", chu_hoa, "ky tu chu hoa")