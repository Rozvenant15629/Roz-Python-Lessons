duong = []
soduong = 0
am = []
soam = 0
khong = 0
ds = []
while True:
    so = input("nhap so nguyen can nhap: ")
    if so == "x":
        break
    ds.append(int(so))
for a in ds:
    if a > 0:
        duong.append(a)
        soduong = soduong + 1
    elif a < 0:
        am.append(a)
        soam = soam + 1
    else:
        khong = khong + 1
print("co so so duong la:", soduong, "va lan luot la:", duong)
print("co so so am la:", soam, "va lan luot la:", am)
print("co so so khong la:", khong)
