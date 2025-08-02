chuoi = input("nhap cac so nguyen bat ki: ")
so = list(map(int, chuoi.split(",")))
ds = []
tong = 0
trungbinhcong = 0
for a in so:
    if a > 0:
        ds.append(a)
        tong = tong + a
    trungbinhcong = tong / 2
print("danh sach cac so duong la:", ds)
print("trung binh cong cua cac so nguyen duong la:", trungbinhcong)
    