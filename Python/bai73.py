def tong_chia_het_cho_3(ds):
    tong = 0
    for so in ds:
        if so % 3 == 0:
            tong = tong + so
    return tong
chuoi = input("nhap day so nguyen, cach nhau bang dau cach: ")
ds = list(map(int, chuoi.split(",")))
ket_qua = tong_chia_het_cho_3(ds)
print("tong cac so chia het cho 3 la:", ket_qua)