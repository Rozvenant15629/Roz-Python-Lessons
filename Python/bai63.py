ds = []
so_duong = []
so_am = []
so_khong = []
while True:
    so = input("nhap so nguyen: ")
    if so == "x":
        break
    ds.append(int(so))
for a in ds:
    if a > 0:
        so_duong.append(a)
    elif a < 0:
        so_am.append(a)
    else:
        so_khong.append(a)
print("tong cac so duong la:", sum(so_duong))
print("tong cac so am la:", sum(so_am))