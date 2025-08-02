def so_lon_nhat(ds):
    return max(ds)
def so_be_nhat_chia_het_cho_3(ds):
    chia_het_3 = [ x for x in ds if x % 3 == 0 ]
    if chia_het_3:
        return min(chia_het_3)
    else:
        return "ko co so chia het cho 3"
def trung_binh(ds):
    return sum(ds) / len(ds)
chuoi = input("nhap chuoi: ")
ds = list(map(int, chuoi.split(",")))
print("so lon nhat la", so_lon_nhat(ds))
print("so be nhat chia het cho 3 la:", so_be_nhat_chia_het_cho_3(ds))
print("trung binh cong cua danh sach la:", trung_binh(ds))