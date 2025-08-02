chuoi = input("nhap cac so nguyen muon xet: ")
ds = list(map(int, chuoi.split(",")))
ds_so_nguyen_duong = []
ds_so_nguyen_am = []
ds_so_khong = []
for a in ds:
    if a > 0:
        ds_so_nguyen_duong.append(a)
    elif a < 0:
        ds_so_nguyen_am.append(a)
    else:
        ds_so_khong.append(a)
print("danh sach so nguyen duong la:", ds_so_nguyen_duong)
print("danh sach so nguyen am la:", ds_so_nguyen_am)
print("danh sach so khong la:", ds_so_khong)
print("tong cua cac so nguyen duong trong danh sach la:", sum(ds_so_nguyen_duong))
print("tong cua cac so nguyen am trong danh sach la:", sum(ds_so_nguyen_am))
print("tong cua danh sach so 0 la:", sum(ds_so_khong))
