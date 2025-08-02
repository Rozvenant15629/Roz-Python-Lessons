chuoi = input("nhap chuoi: ")
ds = list(map(int, chuoi.split(",")))
print("danh sach la:", ds)
print("tong cac chu so trong danh sach la:", sum(ds))