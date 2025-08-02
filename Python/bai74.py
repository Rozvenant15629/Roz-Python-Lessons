def chia_het_cho_3(ds):
    ket_qua = []
    for so in ds:
        if so % 3 == 0:
            ket_qua.append(so)
    return ket_qua
ds = list(map(int, input("nhap cac so can phan loai: ").split(",")))
print("cac so chia het cho 3 la:", chia_het_cho_3(ds))