chuoi = input("nhap cac so nguyen: ")
ds = list(map(int, chuoi.split(",")))
print("so lon nhat trong danh sach la:", max(ds))
print("so be nhat trong danh sach la:", min(ds))