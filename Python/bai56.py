chuoi = input("nhap mot chuoi bat ki can xet: ")
ds = list(chuoi.split())
dem = 0
for a in ds:
    if len(a) > 3:
        dem = dem + 1
print("so tu co nhieu hon 3 ky tu la:", dem)
