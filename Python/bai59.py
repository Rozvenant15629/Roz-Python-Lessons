chuoi = input("nhap vao cac so bat ki: ")
so = list(map(int, chuoi.split(",")))
ds = []
for a in so:
    if a % 3 == 0:
        ds.append(a)
print("danh sach la:", ds)