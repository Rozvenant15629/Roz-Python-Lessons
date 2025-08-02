chan = []
le = []
tong = 0
ds = []
while True:
    so = int(input("nhap so nguyen: "))
    if so == -999 or so == 999:
        break
    ds.append(so)
for a in ds:
    if a % 2 ==  0:
        chan.append(a)
    else:
        le.append(a)
print("danh sach cac so chan la:", chan)
print("tong cac so le la:", sum(le))
    