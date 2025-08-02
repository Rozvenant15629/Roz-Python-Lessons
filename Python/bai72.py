def tong_chu_so(n):
    tong = 0
    for so in str(n):
        so_nguyen = int(so)
        tong = tong + so_nguyen
    return tong
n = int(input("nhap so: "))
ket_qua = tong_chu_so(n)
print("ton cac chu so la:", ket_qua)