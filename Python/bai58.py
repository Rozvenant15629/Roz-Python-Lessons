chuoi = input("nhap vao mot chuoi cac so nguyen: ")
ds = list(map(int, chuoi.split(",")))
tong = 0
chan = []
for a in ds:
    if a % 2 == 0:
        tong = tong + a
        chan.append(a)
print("danh sach cac so chan la:", chan)
print("tong la:", tong)