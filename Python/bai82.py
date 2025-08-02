def nhap_diem():
    chuoi = input("nhap diem: ")
    ds = list(map(float, chuoi.split()))
    return ds
def diem_trung_binh(ds):
    return sum(ds) / len (ds)
def xep_loai(tb):
    if tb >= 8:
        return "Gioi"
    elif tb >= 6.5:
        return "Kha"
    elif tb >= 5:
        return "Trung binh"
    else:
        return "Yeu"
danh_sach_diem = nhap_diem()
tb = diem_trung_binh(danh_sach_diem)
loai = xep_loai(tb)
print("nhap danh sach diem:", danh_sach_diem)
print("diem trung binh la:", round(tb, 2))
print("xep loai:", loai)