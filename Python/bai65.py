so_nguyen_to = 0
ds_so_nguyen_to = []
ds_khong_la_so_nguyen_to = []
ds = []
while True:
    so = input("nhap cac so nguyen: ")
    if so == "x":
        break
    ds.append(int(so))
for a in ds:
    if a < 2:
        ds_khong_la_so_nguyen_to.append(a)
    else:
        nguyen_to = True
        for b in range (2, a):
            if a % b == 0:
                nguyen_to = False
                break
        if nguyen_to:
            ds_so_nguyen_to.append(a)
        else:
            ds_khong_la_so_nguyen_to.append(a)
print("cac so nguyen to lan luot la:", ds_so_nguyen_to)
print("cac so ko la so nguyen to lan luot la:", ds_khong_la_so_nguyen_to)
