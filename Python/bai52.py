chuoi = input("nhap vao mot chuoi so nguyen: ")
so = list(map(int, chuoi.split()))
dem = 0
for a in so:
    if a < 0:
        dem = dem + 1
print("so so am trong day chuoi la:", dem)
