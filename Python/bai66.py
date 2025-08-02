chan = []
le = []
ds = []
while True:
    so = input("nhap so nguyen can phan loai: ")
    if so == "x":
        break
    ds.append(int(so))
for a in ds:
    if a % 2 == 0:
        chan.append(a)
    else:
        le.append(a)
print("danh sach so nguyen chan la:", chan)
print("danh sach so nguyen le la:", le)